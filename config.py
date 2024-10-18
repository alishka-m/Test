from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config('BOTTT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())