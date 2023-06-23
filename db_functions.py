import sqlite3

# Функция для подключения к БД
def create_connection(db_name):
    connect = None
    try:
        connect = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connect


# Функция для создания новой таблицы
def create_table(connect, sql):
    try:
        curses = connect.cursor()
        curses.execute(sql)
    except sqlite3.Error as e:
        print(e)


# Функция для добавления нового продукта в таблицу
def insert_product(connect, product):
    try:
        sql = '''INSERT INTO products(product_title, price, quantity) VALUES (?,?,?)'''
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as e:
        print(e)


# Функция для обновления данных продукта по ID
def update_product(connect, product):
    try:
        if isinstance(product[0], int):
            sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        else:
            sql = '''UPDATE products SET price = ? WHERE id = ?'''
        curses = connect.cursor()
        curses.execute(sql, product)
        connect.commit()
    except sqlite3.Error as e:
        print(e)


# Функция для удаления продукта по ID
def deleted_product(connect, product):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        curses = connect.cursor()
        curses.execute(sql, (product,))
        connect.commit()
    except sqlite3.Error as e:
        print(e)


# Функция для распечатки продуктов по определённым критериям
def select_product(connect, product=None):
    try:
        curses = connect.cursor()
        if isinstance(product, tuple):
            sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
            curses.execute(sql, product)
        elif isinstance(product, str):
            sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
            curses.execute(sql, (product,))
        else:
            sql = '''SELECT * FROM products'''
            curses.execute(sql)

        products = curses.fetchall()
        for product in products:
            print(f'---------------------------\n'
                  f'Идентификатор: {product[0]}\n'
                  f'Название: {product[1]}\n'
                  f'Цена: {product[2]} сом\n'
                  f'Количество: {product[3]}')
    except sqlite3.Error as e:
        print(e)