# 🕵️‍♂️ ZeroTrace: Invisible Keylogger + AI-Based Threat Trap

🚨 **Live Demo (Streamlit App)**:  
👉 [https://keylogger-hxrkblzsf2edh5qobdfi63.streamlit.app/](https://keylogger-hxrkblzsf2edh5qobdfi63.streamlit.app/)

---

ZeroTrace is an advanced cybersecurity and AI-powered deception framework designed to **silently observe**, **log attacker behavior**, and **analyze threats in real-time** using machine learning. It combines a **honeypot**, **encrypted keylogger**, and a **lightweight threat classifier** to detect, track, and report potential attackers or unauthorized activity.

---

## 🚀 Features

- 🎯 **Fake Login Honeypot** — Traps unauthorized users  
- 👀 **Silent Keylogger** — Logs all keystrokes encrypted in the background  
- 🔍 **Behavior Analyzer** — Detects suspicious users using ML model  
- 📄 **Threat Reports** — Generates real-time attacker reports  
- 🧠 **Trained Model** — Lightweight RandomForest classifier with behavioral inputs  
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
├── dashboard.py ← Streamlit dashboard UI
├── requirements.txt ← All required dependencies
└── README.md ← You're here!

---

## ⚙️ How It Works

1. **Fake login page** attracts intruders and collects login behavior  
2. **Keylogger** runs in background to log all keystrokes silently and securely  
3. Behavior like time on page, clicks, unusual inputs is passed to an AI agent  
4. **ML model** classifies whether it's a normal user, suspicious, or attacker  
5. **Reports** are generated with timestamps and verdicts for admin review  

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/Aryanshukla578/Keylogger.git
cd Keylogger
pip install -r requirements.txt
🌐 Run on Streamlit (Cloud Dashboard)
Open the interactive threat dashboard:

🔗 Live Demo:
👉 https://keylogger-hxrkblzsf2edh5qobdfi63.streamlit.app/
🔐 Security Notes
Keystrokes are encrypted before storage

ML model only analyzes behavior — no personal data is stored

Include user consent and privacy policy for real-world deployments

🧩 Future Enhancements
Add real-time intrusion alerts

Browser extension for live threat blocking

Integrate with facial recognition or voice-based ID

Export logs to cloud dashboards or SIEM tools

📃 License
MIT License © Aryan Shukla 2025

🙌 Acknowledgements
scikit-learn for ML

pynput and pickle for input capture and persistence

Streamlit for the web dashboard

Aryan Shukla — making cybersecurity smarter! 🚀

---

Let me know if you'd like help automatically pushing this to GitHub or tweaking the dashboard interface/UI next.
