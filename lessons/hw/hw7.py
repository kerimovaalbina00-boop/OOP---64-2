import sqlite3

# A4
connect = sqlite3.connect("store.db")
# рука с ручкой
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    price INTEGER NOT NULL ,
    quantity INTEGER NOT NULL
)
""")
connect.commit()

def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    connect.commit()
    print("Товар добавлен!")
create_product("Водка", 2000, 80)


def read_products():
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    print(data)

read_products()


def update_product(rowid, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, rowid)
    )
    print("Цена обновлена!")
    connect.commit()

def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    connect.commit()
    print("Товар удален!)