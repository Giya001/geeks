from curses.ascii import isalpha

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import ADMIN


class IsAdmin(BoundFilter):
    async def check(self, messsage: types.Message) -> bool:
        if messsage.from_user.id == int(ADMIN):
            return True
        else:
            return False


class IsLetter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        for letter in message.text:
            if letter.isalpha():
                return True

        return False
