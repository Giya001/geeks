from aiogram import types

from loader import dp, ADMIN,bot
from states import MyAdminStates
from utils.database import users
from filters import IsAdmin


@dp.message_handler(IsAdmin(),commands=['users'])
async def get_user(message: types.Message):
    user = users.get_user()
    print(user)
    for item in user:
        text = (f"<i>FIO</i> - <b> {item[1]}</b>\n"
                f"<i>USERNAME</i> - <b> {item[2]}</b>\n"
                f"<i>CHAT</i> - <b> {item[3]}</b>\n"
                f"<i>PHONE</i> - <b> {item[4]}</b>\n")
        await message.answer(text=text, parse_mode="HTML")


@dp.message_handler(IsAdmin(), commands=['post'])
async def send_post(message: types.Message):
    await message.answer("Xabarni kiriting:")
    await MyAdminStates.message.set()

@dp.message_handler(state=MyAdminStates.message)
async def send_message(message:types.Message):
    if message.from_user.id == int(ADMIN):

        user = users.get_user()
        if len(user) > 0:

            for item in user:
                print(item)
                await bot.send_message(item[2], message.text)

