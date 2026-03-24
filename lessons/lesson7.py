import sqlite3

# A4
connect = sqlite3.connect("users.db")
# рука с ручкой
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS gallery_block(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()


#CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')

    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES (?,?,?)",
        (name, age, hobby)
    )
    connect.commit()
    print('пользователь добавлен!!')

# create_user('Андрей', 15, "Летать")
# create_user('Ardager', 25, "Летать")
# create_user('Arzy', 26, "Летать")
# create_user('Oleg', 12, "Летать")
# create_user('Alex', 33, "Летать")


def read_users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    print(data)
    # for i in data:
    #     print(f"name: {i[0]} age: {i[1]} hobby: {i[2]}")

# read_users()

def update_user(name):
    cursor.execute(
        'UPDATE users SET name = ? WHERE age > 25',
        (name,)
    )
    # cursor.execute(
    #     'UPDATE users SET age = ?',
    #     (age,)
    # )
    connect.commit()
    print("пользователь обнавлен!!")

update_user("Скуфф!!")


def delete_user(id):
    cursor.execute(
        'DELETE FROM users WHERE id = ?',
        (id,)
    )
    connect.commit()
    print("пользователь удален!!")

# delete_user(2)