import psycopg2
from psycopg2 import errors, sql

def create_database_if_not_exists():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="12345",  
            host="localhost",
            port="5432"
        )
        conn.autocommit = True 
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'laba7_db'")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("laba7_db")))
            print("База данных 'laba7_db' создана")
        else:
            print("База данных 'laba7_db' уже существует")
        
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"Ошибка при создании БД: {e}")
        print("Убедитесь, что PostgreSQL запущен и доступен")
        return False

def create_laba7_table():
    try:
        conn = psycopg2.connect(
            dbname="laba7_db",
            user="postgres",
            password="12345",  
            host="localhost",
            port="5432"
        )
        
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS laba7 (
                id SERIAL PRIMARY KEY,
                student_name VARCHAR(100) NOT NULL,
                group_name VARCHAR(20),
                task_number INTEGER,
                score INTEGER CHECK (score >= 0 AND score <= 100)
            )
        ''')
        print("Таблица 'laba7' создана (или уже существует)")
        
        cursor.execute("DELETE FROM laba7")
        print("Старые записи удалены")
        
        test_data = [
            ('Иванов Иван', 'Группа 101', 1, 85),
            ('Петрова Мария', 'Группа 101', 2, 92),
            ('Сидоров Алексей', 'Группа 102', 1, 78),
            ('Козлова Екатерина', 'Группа 102', 3, 95),
            ('Смирнов Дмитрий', 'Группа 103', 2, 88)
        ]
        
        for data in test_data:
            cursor.execute(
                """
                INSERT INTO laba7 
                (student_name, group_name, task_number, score) 
                VALUES (%s, %s, %s, %s)
                """,
                data
            )
        print("Добавлено 5 тестовых записей в таблицу 'laba7'")
        
        print("\nСОДЕРЖИМОЕ ТАБЛИЦЫ 'laba7':")
        
        cursor.execute("""
            SELECT id, student_name, group_name, task_number, score
            FROM laba7 
            ORDER BY id
        """)
        
        records = cursor.fetchall()
        
        print(f"{'ID':3} | {'СТУДЕНТ':20} | {'ГРУППА':10} | {'ЗАДАНИЕ':8} | {'ОЦЕНКА':6}")
        print("-" * 65)
        
        for record in records:
            print(f"{record[0]:3} | {record[1]:20} | {record[2]:10} | {record[3]:8} | "
                  f"{record[4]:6}")
        
        print("\nСТАТИСТИКА:")
        cursor.execute("""
            SELECT 
                COUNT(*) as total,
                AVG(score) as avg_score,
                MIN(score) as min_score,
                MAX(score) as max_score
            FROM laba7
        """)
        stats = cursor.fetchone()
        
        print(f"Всего записей: {stats[0]}")
        print(f"Средний балл: {stats[1]:.1f}")
        print(f"Минимальный балл: {stats[2]}")
        print(f"Максимальный балл: {stats[3]}")
        
        cursor.execute("""
            SELECT group_name, COUNT(*) as students, AVG(score) as avg_score
            FROM laba7
            GROUP BY group_name
            ORDER BY group_name
        """)
        
        print("\nСТАТИСТИКА ПО ГРУППАМ:")
        groups_stats = cursor.fetchall()
        for group in groups_stats:
            print(f"  {group[0]}: {group[1]} студентов, средний балл: {group[2]:.1f}")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("\nРабота с PostgreSQL завершена успешно!")
        
    except errors.OperationalError as e:
        print(f"Ошибка подключения: {e}")
        print("\nПроверьте:")
        print("1. PostgreSQL запущен: sudo systemctl status postgresql")
        print("2. Пароль пользователя postgres правильный")
        print("3. Возможно, нужно изменить пароль в коде на строке 12 и 40")
        
    except Exception as e:
        print(f"Неизвестная ошибка: {repr(e)}")


if create_database_if_not_exists():
    create_laba7_table()
else:
    print("Не удалось создать базу данных. Проверьте настройки PostgreSQL.")
