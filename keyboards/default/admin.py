from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_start_admin():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)

    btn.add(KeyboardButton("/sticker")).insert(KeyboardButton("/statistika")).add(KeyboardButton("/post"))
    btn.add(KeyboardButton("Контакт", request_contact=True))
    btn.add(KeyboardButton("/aboutme")).insert(KeyboardButton("/users"))
    return btn