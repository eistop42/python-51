# функциональный стиль

def sum(a, b):
    """Фyнкция для сложения"""
    return a + b

def minus(a, b):
    """Фyнкция для вычитания"""
    return a - b

def multi(a, b):
    """Фyнкция для умножение"""
    return a * b


while True:
    number_1 = int(input('Первое число: '))
    number_2 = int(input('Второе число: '))
    action = input('Дествие: +-*/: ')

    if action == '+':
        res = sum(number_1, number_2)
    elif action == '-':
        res = minus(number_1, number_2)
    elif action == '*':
        res = multi(number_1, number_2)
    print(res)