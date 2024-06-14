from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_start():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)

    btn.add(KeyboardButton("/sticker")).insert(KeyboardButton("/photo"))
    btn.add(KeyboardButton("Контакт", request_contact=True))
    btn.add(KeyboardButton("/aboutme"))
    return btn