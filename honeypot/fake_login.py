from flask import Blueprint, request, render_template_string
from datetime import datetime
import os

# Create Blueprint for honeypot
honeypot = Blueprint('honeypot', __name__)

# File to log intrusions
LOG_FILE = "honeypot_intrusions.log"

# HTML template for fake login
FAKE_LOGIN_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin Login</title>
    <style>
        body { font-family: Arial, sans-serif; background: #111; color: #fff; text-align: center; padding-top: 10%; }
        .login-box {
            background: #1a1a1a;
            padding: 30px;
            border-radius: 8px;
            display: inline-block;
            box-shadow: 0 0 10px rgba(255, 0, 0, 0.5);
        }
        input { margin: 10px 0; padding: 10px; width: 250px; }
        button { padding: 10px 20px; background: crimson; border: none; color: #fff; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Admin Panel Login</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Admin Username" required><br>
            <input type="password" name="password" placeholder="Admin Password" required><br>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
"""

@honeypot.route("/admin", methods=["GET", "POST"])
def fake_admin_login():
    if request.method == "POST":
        ip = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        username = request.form.get('username')
        password = request.form.get('password')
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"[{timestamp}] IP: {ip}, UA: {user_agent}, USERNAME: {username}, PASSWORD: {password}\n"

        # Write to log file
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        return render_template_string("<h1 style='color:red;'>Unauthorized. This activity has been reported.</h1>")

    return render_template_string(FAKE_LOGIN_HTML)
