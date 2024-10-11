from aiogram import executor
import logging
from config import dp, bot,Admins
from handlers import coomands, quiz, FSM_store, FSM_reg,echo

from db import db_main
async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin,
                               text='Бот включен!')

    await db_main.sql_create()

quiz.register_handler_quiz(dp)
coomands.register_handlers_commands(dp)
FSM_reg.register_handlers_registration(dp)
FSM_store.store_handler_storing(dp)

echo.register_handlers_echo()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)