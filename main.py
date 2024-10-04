import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
import os
from decouple import config

token = config('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands={'start'})
async def command_start(massege: types.Message):
    name = massege.from_user.first_name
    await massege.answer(f"пошел нахуй, {name}!")

@dp.message_handler(commands=['pic'])
async def send_picture(massege: types.Message):
    photo_path = os.path.join("картинки", "photo_2024-10-04_10-35-05.jpg")
    with open(photo_path, "rb") as photo:
        await massege.answer_photo(
        photo=photo,
        caption="пятьдесят два нахуй 🤟🏿"
        )

@dp.message_handler()
async def echo_handler(messsage: types.Message):
    text = messsage.text
    await messsage.answer(text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    #запуск бота
    executor.start_polling(dp)
