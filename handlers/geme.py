from aiogram import Dispatcher, types
from config import bot
import random


games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def game_dice(message : types.Message):
    await bot.send_dice(chat_id=message.from_user.id, emoji=random.choice(games))


def register_game_handlers(dp : Dispatcher):
    dp.register_message_handler(game_dice, commands=['game'])
