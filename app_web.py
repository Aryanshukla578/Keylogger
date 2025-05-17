from flask import Flask, render_template
import os

app = Flask(__name__)
LOG_FILE = "zerotrace/logger/logs.txt"  # Adjust path if needed

@app.route("/")
def index():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.read().splitlines()
    else:
        logs = ["No logs found."]
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
