import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM users")
conn.commit()
cursor.execute("INSERT INTO users (name, age) VALUES ('Иван', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Мария', 30)")
conn.commit()

print("=== ДАННЫЕ ДО УДАЛЕНИЯ ===")
cursor.execute("SELECT * FROM users")
users_before = cursor.fetchall()
for user in users_before:
    print(f"ID: {user[0]}, Имя: {user[1]}, Возраст: {user[2]}")

print("\nУдаляем пользователя 'Иван'...")
cursor.execute("DELETE FROM users WHERE name = ?", ('Иван',))
conn.commit()
print("Запись удалена.")

print("\n=== ДАННЫЕ ПОСЛЕ УДАЛЕНИЯ ===")
cursor.execute("SELECT * FROM users")
users_after = cursor.fetchall()

if users_after:
    for user in users_after:
        print(f"ID: {user[0]}, Имя: {user[1]}, Возраст: {user[2]}")
else:
    print("В таблице нет записей")

conn.close()
