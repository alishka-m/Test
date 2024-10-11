from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz_1(message: types.Message):
    keyboard = inlineKeyboardMarkup(resize_keyboard=True)
    button = inlineKeyboardButton('Далее', callback_data='quiz1')

    keyboard.add(button)

    question = 'BMW or Mersedes or Audi'

    answer = ['BMW', "Mersedes", "Audi"]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Aуди лучше!',
        open_period=20,
        reply_markup=keyboard
    )

async def quiz_2(call: types.CallbackQuery):
    question = 'Сколько хромосом у человека'
    answer = ['54', '67', '46', '15']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='ye ye!',
        open_period=20,
    )


def register_handler_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])