from aiogram.dispatcher.filters.state import StatesGroup, State


class MyStates(StatesGroup):
    about = State()
    number = State()
    info = State()


class MyAdminStates(StatesGroup):
    message=State()