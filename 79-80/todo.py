import sqlite3

def get_user(name):
    with sqlite3.connect('db') as conn:
        cur = conn.cursor()
        cur.execute('select * from users where name = ?', (name, ))
        res = cur.fetchone()
        return res

def add_task(task_name, user_id):
    with sqlite3.connect('db') as conn:
        cur = conn.cursor()
        cur.execute('insert into tasks (name, user_id) values (?, ?)', (task_name, user_id))
        conn.commit()


name = input('Введи имя: ')
user = get_user(name)
if user:
    print(f'Привет {user[1]} Начинаем работу')
    while True:
        print('Выбери действие: ')
        print('1 - добавить задачу')
        action = input('выбирай: ')
        if action == '1':
            name = input('Название задачи')
            add_task(name, user[0])
            print('Задача добавлена')
else:
    print('нужна регистрация')
# сходить в базу и проверить, есть ли такой пользователь