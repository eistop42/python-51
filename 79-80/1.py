import sqlite3

# создание подключения
conn = sqlite3.connect('db')

# создание курсора для транзакций-запросов
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS USERS  (
            id integer primary key autoincrement, name text not null)"""
            )
cur.execute("""CREATE TABLE IF NOT EXISTS TASKS (
            id integer primary key autoincrement, 
            name text not null,
            user_id integer not null,
            FOREIGN KEY (user_id) REFERENCES USERS(id)
            )
            """
            )
# выполнение транзакции
conn.commit()

# добавление пользователя
cur.execute('INSERT INTO USERS (name) VALUES ("alisa")')
conn.commit()

# закрытие подключения
conn.close()

