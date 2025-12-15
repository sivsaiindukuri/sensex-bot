from telethon import TelegramClient, events
from signal_parser import parse_signal

def start_listener(api_id, api_hash, phone, channel_id, callback):
    client = TelegramClient("telegram", api_id, api_hash)

    @client.on(events.NewMessage(chats=channel_id))
    async def handler(event):
        signal = parse_signal(event.text)
        if signal:
            await callback(signal)

    client.start(phone=phone)
    client.run_until_disconnected()