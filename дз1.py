import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from decouple import config

token = config('BOTTT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands={'start'})
async def command_start(massege: types.Message):
    name = massege.from_user.first_name
    await massege.answer(f"geeks на всегда, {name}!")


@dp.message_handler()
async def echo_handler(massege: types.Message):
    text = massege.text
    try:
        number = float(text)
        squared = number ** 2
        await massege.answer(f"Квадрад числа {number} равен {squared}.")
    except ValueError:
        await massege.answer(text)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    #запуск бота
    executor.start_polling(dp)
