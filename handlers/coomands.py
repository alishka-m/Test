from aiogram import types, Dispatcher
import os

async def command_start(massege: types.Message):
    name = massege.from_user.first_name
    await massege.answer(f"geeks на всегда, {name}!")

await message.answer(f'Добро пожалавать {name} чем могу помочь?')
    await bot.send_message(chat_id=message.from_user.id, text=f'Твой телеграм ID - {message.from_user.id}')

async def send_picture_handler(message: types.Message):
    photo_path = os.path.join("images", "cat.webp")
    with open(photo_path, "rb") as photo:
        await message.answer_photo(
            photo=photo,
            caption="ААААААААА!!!!!"
        )

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start_handler, commands=['start'])
    dp.register_message_handler(send_picture_handler, commands=['pic'])
