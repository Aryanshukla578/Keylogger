import os
import json
import base64
from cryptography.fernet import Fernet
from datetime import datetime

# Paths
REPORTS_DIR = "zerotrace/reports"
KEY_FILE = "zerotrace/utils/.reportkey"

# Load or generate encryption key
def load_key():
    # Ensure the directory for the key file exists
    os.makedirs(os.path.dirname(KEY_FILE), exist_ok=True)

    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

fernet = load_key()

# Save encrypted report
def save_report(data: dict, report_name=None):
    # Ensure the reports directory exists
    os.makedirs(REPORTS_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = report_name or f"threat_report_{timestamp}.enc"
    file_path = os.path.join(REPORTS_DIR, filename)

    try:
        json_data = json.dumps(data).encode()
        encrypted = fernet.encrypt(json_data)

        with open(file_path, "wb") as f:
            f.write(encrypted)
        print(f"[✓] Encrypted report saved to {file_path}")
    except Exception as e:
        print(f"[!] Failed to save encrypted report: {e}")

# Read and decrypt report
def read_report(file_path):
    try:
        with open(file_path, "rb") as f:
            encrypted = f.read()
        decrypted = fernet.decrypt(encrypted)
        return json.loads(decrypted)
    except Exception as e:
        print(f"[!] Error reading report: {e}")
        return None

# Debug usage
if __name__ == "__main__":
    sample_data = {
        "module": "honeypot",
        "ip": "192.168.1.15",
        "payload": "<script>alert('xss')</script>",
        "timestamp": str(datetime.now())
    }
    save_report(sample_data)
