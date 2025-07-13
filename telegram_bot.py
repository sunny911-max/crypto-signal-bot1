import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load from .env file if present

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("BOT_TOKEN or CHAT_ID not set.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        print("Telegram response:", response.status_code, response.text)
    except Exception as e:
        print("Failed to send message:", e)
