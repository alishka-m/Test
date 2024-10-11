CREATE_TABLE_STORE = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    photo TEXT
    )
"""

INSERT_STORE_QUERY = """
 INSERT INTO store (name_product, size, praice, photo)
 VALUES (?, ?, ?)
"""