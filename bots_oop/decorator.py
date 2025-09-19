
def check_user(function_name):
    """Проверить аргументы функции.
    Вызывать ее, если имя допустимо"""
    def func(name):
        print('Проверяем имя...')
        print('Вызываем исходную функцию')
        if name != 'Боб':
            return function_name(name)
        else:
            print('Кажется, ты Боб')
    return func

@check_user
def hello(name):
    print(f'Привет, {name}')


@check_user
def buy(name):
    print(f'Пока, {name}')


hello('Алиса')
hello('Боб')
buy('Боб')
