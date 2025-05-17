import os
import json
import base64
from cryptography.fernet import Fernet
from datetime import datetime

# Path to save reports
REPORTS_DIR = "zerotrace/reports"
KEY_FILE = "zerotrace/utils/.reportkey"

# Generate or load encryption key
def load_key():
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
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

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

# (Optional) Read and decrypt report for debugging
def read_report(file_path):
    try:
        with open(file_path, "rb") as f:
            encrypted = f.read()
        decrypted = fernet.decrypt(encrypted)
        return json.loads(decrypted)
    except Exception as e:
        print(f"[!] Error reading report: {e}")
        return None

# Example usage (for debugging)
if __name__ == "__main__":
    sample_data = {
        "module": "honeypot",
        "ip": "192.168.1.15",
        "payload": "<script>alert('xss')</script>",
        "timestamp": str(datetime.now())
    }
    save_report(sample_data)
