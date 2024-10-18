import sqlite3

from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print('data base is ready!')

    cursor.execute(queries.CREATE_TABLE_STORE)
    cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAILS)


async def sql_insert_product(product_id, product_name, size, price, photo, category, info_product):
    cursor.execute(queries.INSERT_DETAILS_QUERY, (product_id, category, info_product))
    cursor.execute(queries.INSERT_STORE_QUERY, (product_id, product_name, size, price, photo))
    db.commit()


def sql_select_product() -> dict:
    products = cursor.execute(queries.INPUT_PRODUCTS_QUERY).fetchall()
    filtered_products = []
    for product in products:
        row = {
            'id': product[0],
            'product_name': product[2],
            'size': product[3],
            'price': product[4],
            'photo': product[5],
            'category': product[7],
            'info': product[-1],
            'product_id': product[1]
        }
        filtered_products.append(row)

    return filtered_products