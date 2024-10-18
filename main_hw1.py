from aiogram import Dispatcher, Bot, executor, types
from decouple import config

TOKEN = config('BOT_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message : types.Message):
    try:
        await message.answer(int(message.text)**2)
    except ValueError:
        await message.answer(message.text)


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)