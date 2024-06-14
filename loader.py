import os

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
from aiogram.contrib.fsm_storage.memory import MemoryStorage
CHANNELS=[{"name":"exam_checks","chanel_id":"-1002184378781"}]
storage = MemoryStorage()
ADMIN = os.getenv('ADMIN')
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot, storage=storage)
