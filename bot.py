import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Setup logging to file and console
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "MOCK_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    logging.info(f"User {message.from_user.id} started the bot.")
    await message.answer("Hello! I am a stub bot. CI/CD is working correctly! 🚀")

@dp.message()
async def echo_mock(message: types.Message):
    logging.info(f"Received message: {message.text}")
    await message.answer("Static response: The service is currently under development.")

async def main():
    logging.info("Stub bot successfully started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
