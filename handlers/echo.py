from aiogram import types, Dispatcher

async def echo_handler(message : types.Message):
    text = message.text
    await message.answer(text)


def register_handler_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)