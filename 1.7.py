import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("DROP TABLE IF EXISTS cars")
cursor.execute("DROP TABLE IF EXISTS cities")

cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course INTEGER
)
''')

cursor.execute('''
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    year INTEGER,
    pages INTEGER
)
''')

cursor.execute('''
CREATE TABLE cars (
    car_id INTEGER PRIMARY KEY,
    brand TEXT NOT NULL,
    model TEXT,
    color TEXT,
    price REAL
)
''')

cursor.execute('''
CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT,
    population INTEGER,
    area REAL
)
''')


cursor.execute("INSERT INTO students (id, name, age, course) VALUES (1, 'Алексей', 20, 2)")
cursor.execute("INSERT INTO students (id, name, age, course) VALUES (2, 'Мария', 21, 3)")
cursor.execute("INSERT INTO students (id, name, age, course) VALUES (3, 'Иван', 19, 1)")

cursor.execute("INSERT INTO books (book_id, title, author, year, pages) VALUES (1, 'Мастер и Маргарита', 'Булгаков', 1967, 480)")
cursor.execute("INSERT INTO books (book_id, title, author, year, pages) VALUES (2, 'Преступление и наказание', 'Достоевский', 1866, 672)")
cursor.execute("INSERT INTO books (book_id, title, author, year, pages) VALUES (3, 'Война и мир', 'Толстой', 1869, 1225)")

cursor.execute("INSERT INTO cars (car_id, brand, model, color, price) VALUES (1, 'Toyota', 'Camry', 'Белый', 2500000)")
cursor.execute("INSERT INTO cars (car_id, brand, model, color, price) VALUES (2, 'Lada', 'Vesta', 'Серый', 1200000)")
cursor.execute("INSERT INTO cars (car_id, brand, model, color, price) VALUES (3, 'BMW', 'X5', 'Черный', 5000000)")

cursor.execute("INSERT INTO cities (city_id, name, country, population, area) VALUES (1, 'Москва', 'Россия', 13000000, 2561)")
cursor.execute("INSERT INTO cities (city_id, name, country, population, area) VALUES (2, 'Санкт-Петербург', 'Россия', 5600000, 1439)")
cursor.execute("INSERT INTO cities (city_id, name, country, population, area) VALUES (3, 'Новосибирск', 'Россия', 1600000, 505)")

conn.commit()

print("СОДЕРЖИМОЕ ТАБЛИЦ:\n")

print("1. Таблица 'students' (студенты):")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(f"   ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}, Курс: {row[3]}")

print("\n2. Таблица 'books' (книги):")
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(f"   ID: {row[0]}, Название: '{row[1]}', Автор: {row[2]}, Год: {row[3]}, Страниц: {row[4]}")

print("\n3. Таблица 'cars' (автомобили):")
cursor.execute("SELECT * FROM cars")
for row in cursor.fetchall():
    print(f"   ID: {row[0]}, Марка: {row[1]}, Модель: {row[2]}, Цвет: {row[3]}, Цена: {row[4]:,.0f} руб.")

print("\n4. Таблица 'cities' (города):")
cursor.execute("SELECT * FROM cities")
for row in cursor.fetchall():
    print(f"   ID: {row[0]}, Город: {row[1]}, Страна: {row[2]}, Население: {row[3]:,}, Площадь: {row[4]} км²")

conn.close()

print("\nСоздано 4 таблицы!")