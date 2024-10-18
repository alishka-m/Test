import sqlite3
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM store s 
    INNER JOIN detail_store ds 
    ON s.product_id = ds.product_id 
    """).fetchall()
    conn.close()
    return products

async def  start_send_products(message: types,Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    button_all = types.InlineKeyboardButton('Load all products')
    button_one = types.InlineKeyboardButton('Load by one')
    keyboard.add(button_all, button_one)

    await message.answer('Choose how will load products:',
                         reply_markup=keyboard)

async def sendall_products(callback_query: types.CallbackQuery):
        products = fetch_all_products()

        if products:
            for product in products:
                caption = (f'Ваш товар:\n'
                f'Название товара: {product["product_name"]}\n'
                f'Размер: {product["size"]}\n'
                f'Категория: {product["category"]}\n'
                f'Цена: {product["price"]}\n'
                f'инфо: {product["info"]}\n'
                f'уникальное значение: {product["id"]}')

            await callback_query.message.answer_photo(
                photo=product["photo"],
                caption=caption
            )
        else:
            await callback_query.message.answer('Товара нет!')

def register_send_products_handlers(db: Dispatcher):
    db.register_message_handler(start_send_products, commands=['products'])
    db.register_callback_query_handler(sendall_products,
                                                     Text(equals='all')