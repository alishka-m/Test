from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
import os
import logging

logging.basicConfig(level=logging.INFO)


async def quiz_1(message: types.Message):
    # Создание клавиатуры
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='quiz_2')
    keyboard.add(button)

    # Вопрос и варианты ответа
    question = 'BMW, Mercedes или Audi?'
    answer = ['BMW', 'Mercedes', 'Audi']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Audi лучше!',
        open_period=20,
        reply_markup=keyboard
    )


async def quiz_2(call: types.CallbackQuery):
    question = 'Сколько хромосом у человека?'
    answer = ['54', '67', '46', '15']
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button_1 = InlineKeyboardButton('Далее', callback_data='next')
    button_2 = InlineKeyboardButton('Отмена', callback_data='cancel')
    keyboard.add(button_1, button_2)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Правильный ответ: 46!',
        open_period=20,
        reply_markup=keyboard
    )


async def quiz_3(call: types.CallbackQuery):
    photo_path = os.path.join("img", "linux.jpeg")
    question = 'Кто основал ОС Linux?'
    answer = ['Линус Торвальдс', 'Марк Цукерберг', 'Гвидо ван Россум', 'Павел Дуров']

    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button_1 = InlineKeyboardButton('Далее', callback_data='next_2')
    button_2 = InlineKeyboardButton('Отмена', callback_data='cancel')

    keyboard.add(button_1, button_2)
    with open(photo_path, "rb") as photo:
        await bot.send_photo(chat_id=call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Линус Торвальдс основал Linux в 1991 году.",
        open_period=30,
        reply_markup=keyboard
    )


async def quiz_4(call: types.CallbackQuery):
    photo_path = os.path.join("img", "python.jpeg")
    question = 'Кто основал ЯП "Python"?'
    answer = ['Линус Торвальдс', 'Марк Цукерберг', 'Гвидо ван Россум', 'Павел Дуров']

    with open(photo_path, "rb") as photo:
        await bot.send_photo(chat_id=call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Основателем Python является 'Гвидо ван Россум'",
        open_period=30
    )


def register_handlers_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='quiz_2')  # Указываем обработку по 'quiz_2'
    dp.register_callback_query_handler(quiz_3, text='next')  # И для 'next'
    dp.register_callback_query_handler(quiz_4, text='next_2')  # И для 'next'