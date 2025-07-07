from telegram_notifier import send_telegram_message

@app.route('/')
def home():
    send_telegram_message("📡 Manual Signal Test from BossView 4.5")
    return "BossView 4.5 Running"
