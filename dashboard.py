import streamlit as st
import os
import json
from datetime import datetime
from collections import Counter
import pandas as pd
from utils import report

LOG_FILE = "zerotrace/logger/logs.txt"
REPORTS_DIR = "zerotrace/reports"

st.set_page_config(page_title="ZeroTrace Dashboard", layout="wide")
st.title("🛡️ ZeroTrace AI Security Dashboard")
st.markdown("Real-time monitoring & threat reports")

# === Utility Functions ===

def count_keystrokes(logs):
    return sum(len(line) for line in logs)

def parse_keystroke_times(logs):
    # Fake timestamps based on line order (simulate 1s gap)
    timestamps = [datetime.now().replace(microsecond=0) for _ in logs]
    data = {"Timestamp": timestamps, "Keystrokes": [len(line) for line in logs]}
    return pd.DataFrame(data)

# === Logs Viewer ===
st.subheader("📋 Keystroke Logs")

logs = []
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        logs = f.read().splitlines()

    if logs:
        st.text_area("Logged Keystrokes", "\n".join(logs), height=200)
    else:
        st.info("No logs recorded yet.")
else:
    st.warning("Log file not found.")

# === Metrics Row ===
st.subheader("📈 Key Metrics")
col1, col2, col3 = st.columns(3)

total_keys = count_keystrokes(logs)
total_reports = len([f for f in os.listdir(REPORTS_DIR) if f.endswith(".enc")]) if os.path.exists(REPORTS_DIR) else 0
last_activity = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if logs else "N/A"

col1.metric("Total Keystrokes", total_keys)
col2.metric("Reports Generated", total_reports)
col3.metric("Last Activity", last_activity)

# === Keystroke Chart ===
st.subheader("📊 Keystroke Activity (Simulated)")
if logs:
    df = parse_keystroke_times(logs)
    st.line_chart(df.set_index("Timestamp"))
else:
    st.info("Chart unavailable: No keystrokes recorded.")

# === Report Viewer ===
st.subheader("📄 Threat Reports")

if os.path.exists(REPORTS_DIR):
    report_files = [f for f in os.listdir(REPORTS_DIR) if f.endswith(".enc")]
    if report_files:
        selected = st.selectbox("Select a report to decrypt", report_files)
        if selected:
            report_data = report.read_report(os.path.join(REPORTS_DIR, selected))
            if report_data:
                st.json(report_data)
            else:
                st.error("Failed to decrypt or read report.")
    else:
        st.warning("No encrypted reports found.")
else:
    st.warning("Reports directory not found.")

# === System Status ===
st.subheader("✅ System Status")
st.success("Honeypot & Logger modules are active")
st.code("AI Agent monitoring behavior in background", language="markdown")
