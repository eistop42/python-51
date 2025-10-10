import sqlite3
from contextlib import contextmanager

class DB():
    def __init__(self, db_name):
        self.db_name = db_name

    @contextmanager
    def sqlconnect(self):
        print(f"Создаем подключение к базе...")
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        yield cursor  # передача курсора внутрь блока with
        print(f"Коммит. Закрываем подключение")
        conn.commit()
        conn.close()

    def get_user(self, name):
        with self.sqlconnect() as cur:
            cur.execute('select * from users where name = ?', (name,))
            res = cur.fetchone()
            return res

    def add_task(self, task_name, user_id):
        with self.sqlconnect() as cur:
            cur.execute('insert into tasks (name, user_id) values (?, ?)', (task_name, user_id))

    def get_tasks(self, user_id):
        """Возвращать задачи пользователя"""
        with self.sqlconnect() as cur:
            cur.execute('select * from tasks where user_id = ?', (user_id,))
            res = cur.fetchall()
            return res

    def add_user(self, name):
        with self.sqlconnect() as cur:
            cur.execute('insert into users (name) values (?)', (name,))
