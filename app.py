from flask import Flask
from honeypot.fake_login import honeypot

app = Flask(__name__)

# Register honeypot blueprint
app.register_blueprint(honeypot)

@app.route("/")
def index():
    return "<h1>Welcome to ZeroTrace AI Security Suite</h1><p>System is actively monitoring...</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
