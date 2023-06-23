from random import uniform, randint
import db_functions as db

# Название БД для подключения
database = 'hw.db'

# Для создания таблицы
create_products_table_sql = '''
CREATE TABLE products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

# Подключение к БД
connection = db.create_connection(database)

if connection is not None:
    print('Connection!')

    # Создание таблицы Products
    db.create_table(connection, create_products_table_sql)

    # Добавление данных в таблицу
    products = ["Яблоко", "Апельсин", "Банан", "Груша", "Киви",
                "Манго", "Ананас", "Клубника", "Гранат", "Арбуз",
                "Авокадо", "Лимон", "Вишня", "Грейпфрут", "Персик"]
    for product in products:
        price = round(uniform(50, 150), 2)
        quantity = randint(1, 10)
        db.insert_product(connection, (product, price, quantity))

    # Изменение данных таблицы по id их quantity
    id_product = 1
    new_quantity = 9
    db.update_product(connection, (new_quantity, id_product))

    # Изменение данных таблицы по id их price
    id_product = 2
    new_price = 66.66
    db.update_product(connection, (new_price, id_product))

    # Удаление данных таблицы по id
    id_product = 4
    db.deleted_product(connection, id_product)

    # Распечатка всех товаров из БД
    db.select_product(connection)

    # Распечатка всех товаров из БД товары, которые дешевле 100 сомов и количество больше 5
    db.select_product(connection, (100, 5))

    # Распечатка товаров по название
    search = 'ан'
    db.select_product(connection, f'%{search}%')

    # Закрытие БД
    connection.close()