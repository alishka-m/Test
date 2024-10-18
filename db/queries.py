CREATE_TABLE_STORE = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    product_id INTEGER,
    name_product varchar(255),
    size varchar(255),
    price varchar(255),
    photo TEXT
)
"""

CREATE_TABLE_PRODUCT_DETAILS = """
CREATE TABLE IF NOT EXISTS product_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    category varchar(255),
    info_product varchar(255)
)
"""

INSERT_STORE_QUERY = """
    INSERT INTO store (product_id, name_product, size, price, photo)
    VALUES (?, ?, ?, ?, ?)
"""

INSERT_DETAILS_QUERY = """
    INSERT INTO product_details (product_id, category, info_product)
    VALUES (?, ?, ?)
"""

INPUT_PRODUCTS_QUERY = """
    SELECT * FROM store
    JOIN product_details ON store.product_id = product_details.product_id
"""