import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")  # если нужно
PASSWORD = os.getenv("PASSWORD")  # если есть 2FA
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # например: -1001234567890

client = TelegramClient("save_id_session", API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    if event.out:
        return  # Пропускаем свои сообщения (бота)

    text = event.raw_text.strip()
    
    if text.isdigit() and 1 <= len(text) <= 9:
        try:
            await client.send_message(CHANNEL_ID, text)
            await event.respond("✅ ID сохранён в канал.")
        except Exception as e:
            await event.respond(f"❌ Ошибка при отправке в канал: {e}")



async def main():
    await client.start(password=PASSWORD)
    print("✅ Клиент запущен!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
