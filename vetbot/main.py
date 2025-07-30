import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import config  # Предполагается, что у вас есть config.py

bot = Bot(token=config.TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет как дела пожалуйста скинь ножки пользователю @a501id5ix спасибо")

async def main():
    print("Бот запущен!")  # Для проверки в логах
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())