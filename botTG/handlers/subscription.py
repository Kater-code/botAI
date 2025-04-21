from aiogram import Router, types
from aiogram.filters import Command
from database.db import activate_subscription

subscription_router = Router()

@subscription_router.message(Command('subscribe'))
async def subscribe_handler(message: types.Message):
    user_id = message.from_user.id
    activate_subscription(user_id, days=30)
    await message.answer("Поздравляем! Ваша подписка активирована на 30 дней!")