import json

with open('db.json') as f:
    users = json.load(f)

user_login = input('Введи логин')
user_passw = input('Введи пароль')

find = False
for user in users:
    if user_login == user['name'] and user_passw == user['password']:
        find = True
if find:
    print('Разршен')
else:
    print('Запрешен')