users = {'tom': '1dfs23', 'sam': '12d3451', 'petr': 'dfe1232'}

user_password = input('Введи пароль: ') #1dfs23
user_login = input('Введи логин: ') #tom

if users[user_login] == user_password:
    print('верный пароль')
else:
    print('неверный логин или пароль')