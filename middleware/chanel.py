from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import CHANNELS, bot


class ChannelMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        print(message.text)
        user = message.from_user
        if user.username:
            ibtn = InlineKeyboardMarkup()
            for chanel in CHANNELS:
                user_channel = await bot.get_chat_member(user_id=int(user.id), chat_id=chanel.get("chanel_id"))
                if user_channel.status == "left":
                    ibtn.add(InlineKeyboardButton(text=chanel.get('name'), url=f"https://t.me/{chanel.get('name')}"))
                    await message.answer('Iltimos kanalga azo boling', reply_markup=ibtn)
                    raise CancelHandler()
class MiddleWare(BaseMiddleware):
    async def on_process_message(self,message:types.Message,data:dict):
        print(f'Qabul qilingan xabar{message.from_user.id}:{message.text}')