import os
import asyncio
from telethon_listener import start_listener
from notifier import notify

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("NOTIFY_CHAT_ID")

async def on_signal(signal):
    await notify(BOT_TOKEN, CHAT_ID, f"✅ Signal received:\n{signal}")

if __name__ == "__main__":
    start_listener(
        int(os.getenv("TG_API_ID")),
        os.getenv("TG_API_HASH"),
        os.getenv("TG_PHONE"),
        int(os.getenv("TG_CHANNEL_ID")),
        on_signal
    )