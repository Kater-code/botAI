from aiogram import Router, types, F
from aiogram.filters import Command
from database.db import add_user

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    add_user(user_id)
    await message.answer("Привет! Добро пожаловать в нашего бота с ИИ!")