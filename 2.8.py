import psycopg2
import time

cache = {}

def simple_cache(query):
    if query in cache:
        print(f"Берем из КЭША: {query}")
        return cache[query]
    
    print(f"Запрос к БД: {query}")
    
    conn = psycopg2.connect(
        dbname="laba7_db",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    
    cache[query] = result
    
    cursor.close()
    conn.close()
    
    return result

conn = psycopg2.connect(
    dbname="laba7_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        score INTEGER
    )
''')

cursor.execute("DELETE FROM students")
cursor.execute("INSERT INTO students (name, score) VALUES ('Иван', 85)")
cursor.execute("INSERT INTO students (name, score) VALUES ('Мария', 92)")
cursor.execute("INSERT INTO students (name, score) VALUES ('Алексей', 78)")

conn.commit()
cursor.close()
conn.close()

print("Таблица создана, добавлено 3 студента\n")

query = "SELECT * FROM students"

print("Запрос 1:")
result1 = simple_cache(query)
print(f"   Результат: {len(result1)} строк\n")

print("Запрос 2:")
result2 = simple_cache(query)
print(f"   Результат: {len(result2)} строк\n")

print("Запрос 3:")
result3 = simple_cache(query)
print(f"   Результат: {len(result3)} строк\n")

print("Запрос 4 :")
result4 = simple_cache(query)
print(f"   Результат: {len(result4)} строк\n")


print(" Содержимое таблицы:")
for row in result1:
    print(f"   {row[0]}. {row[1]} - {row[2]} баллов")
