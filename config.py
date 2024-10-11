from aiogram import Dispatcher, Bot
from decouple import config

Admins=[]

token = config('BOTTT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)