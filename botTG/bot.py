import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers.start import start_router
from handlers.subscription import subscription_router
from handlers.ai_logic import ai_router

# Настройка логирования
logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем роутеры
    dp.include_router(start_router)
    dp.include_router(subscription_router)
    dp.include_router(ai_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())