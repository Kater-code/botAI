from aiogram import Router, types
from services.ai_service import ask_gpt
from database.db import get_user_data, increment_usage, is_subscription_active
from config import FREE_TRIAL_LIMIT

ai_router = Router()

@ai_router.message()
async def ai_message_handler(message: types.Message):
    user_id = message.from_user.id

    user = get_user_data(user_id)

    if user is None:
        await message.answer("Пожалуйста, напишите /start для начала работы.")
        return

    if not is_subscription_active(user):
        if user['usage_count'] >= FREE_TRIAL_LIMIT:
            await message.answer("Ваш бесплатный лимит исчерпан. Оформите подписку для продолжения.")
            return
        increment_usage(user_id)

    try:
        response = await ask_gpt(message.text)
        await message.answer(response)
    except Exception as e:
        await message.answer(f"Произошла ошибка при запросе к ИИ: {e}")