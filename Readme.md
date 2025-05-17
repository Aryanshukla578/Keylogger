# 🕵️‍♂️ ZeroTrace: Invisible Keylogger + AI-Based Threat Trap

ZeroTrace is an advanced cybersecurity and AI-powered deception framework designed to **silently observe**, **log attacker behavior**, and **analyze threats in real-time** using machine learning. It combines a **honeypot**, **encrypted keylogger**, and a **lightweight threat classifier** to detect, track, and report potential attackers or unauthorized activity.

---

## 🚀 Features

- 🎯 **Fake Login Honeypot** — traps unauthorized users
- 👀 **Silent Keylogger** — logs all keystrokes encrypted in background
- 🔍 **Behavior Analyzer** — detects suspicious users using ML model
- 📄 **Threat Reports** — generates real-time attacker reports
- 🧠 **Trained Model** — lightweight RandomForest classifier with behavioral inputs
- 🛡️ **Modular** — Easily extendable for other detection strategies

---

## 📁 Project Structure

zerotrace/
├── ai_agent/
│ ├── behavior_analyzer.py ← ML behavior classification logic
│ ├── train_model.py ← Model training script
│ └── model.pkl ← Trained RandomForest model
├── honeypot/
│ └── fake_login.py ← Trap login page for unauthorized users
├── logger/
│ └── keylogger.py ← Encrypted keylogger (runs silently)
├── utils/
│ └── report.py ← Generates reports from logs
├── app.py ← Main controller to run everything
├── requirements.txt ← All required dependencies
└── README.md ← You're here!

---

## ⚙️ How It Works

1. **Fake login page** attracts intruders and collects login behavior.
2. **Keylogger** runs in background to log all keystrokes silently and securely.
3. Behavior like page time, clicks, unusual inputs is passed to an AI agent.
4. **ML model** classifies whether it's a normal user, suspicious, or attacker.
5. **Reports** are generated with timestamps and verdicts for admin review.

---

## 🛠️ Installation
```bash
git clone https://github.com/your-username/zerotrace.git
cd zerotrace
pip install -r requirements.txt
------
Train the AI Model (Optional)
If you want to retrain the ML behavior model:
bash
python zerotrace/ai_agent/train_model.py
This saves a new model.pkl using simulated behavior data
-------
Run the System
bash
python app.py
This launches:
The fake login honeypot
The keylogger
The ML threat analyzer
---------------------
🧪 Simulated Dataset (used in train_model.py)
python
# Features: [time_on_page, click_count, unusual_inputs, repeated_paths]
X = [[5, 1, 0, 0], [120, 20, 1, 1], [10, 3, 0, 0], [200, 50, 1, 1], [3, 0, 0, 0], [180, 35, 1, 1]]
# Labels: 0 = Normal user, 1 = Threat
y = [0, 1, 0, 1, 0, 1]
📸 Screenshots (Add your own)
----------------------
🔐 Security Notes
Keystrokes are stored in encrypted logs (keylogger.py)

Model only classifies behavior — does not store personal info

Add user consent and usage policy if deployed in real-world settings

🧩 Future Enhancements
Add intrusion alert system

Browser-level extension to block threats

Integration with facial recognition or user behavior analytics

Export logs to cloud dashboard
------
📃 License
MIT License © Aryan Shukla 2025
------
🙌 Acknowledgements
Scikit-learn for ML models
Python’s pynput and pickle for logging and persistence
Aryan Shukla — for making the internet safer! 🚀
