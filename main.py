from aiogram import executor
import logging
from config import dp
from handlers import commands, echo, quiz, geme, FSM_reg, FSM_store, sande_products
from db import db_main

async def on_startup(_):
    await db_main.sql_create()

FSM_store.register_store_handlers(dp) # регистрируем обработчики
commands.register_handlers_commands(dp)
quiz.register_handlers_quiz(dp)
FSM_reg.register_fsm_handlers(dp)
geme.register_game_handlers(dp)
sande_products.register_send_products_handler(dp)

echo.register_handler_echo(dp)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
                               allowed_updates=['callback'])