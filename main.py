from flask import Flask
import os
import requests

app = Flask(__name__)

# Inline Telegram function — no extra module needed
def send_telegram_message(message):
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    
    if TELEGRAM_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": message
        }
        response = requests.post(url, json=data)
        print("Telegram response:", response.text)
    else:
        print("Missing TELEGRAM_TOKEN or CHAT_ID in env.")

@app.route('/')
def home():
    send_telegram_message("🚨 Manual signal test from BossView 4.5 — LIVE!")
    return "BossView 4.5 Running with Telegram 🔥"

if __name__ == "__main__":
    app.run(debug=True)
