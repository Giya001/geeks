from aiogram.types import InlineKeyboardMarkup, KeyboardButton


async def get_voice():
    ibtn = InlineKeyboardMarkup()
    ibtn.add(KeyboardButton("👍", callback_data="like"))
    ibtn.add(KeyboardButton("👎", callback_data="dislike"))
    return ibtn
