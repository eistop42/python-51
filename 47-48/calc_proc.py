
while True:
    number_1 = int(input('Первое число: '))
    number_2 = int(input('Второе число: '))
    action = input('Дествие: +-*/: ')

    if action == '+':
        res = number_1 + number_2
        print(res)
    elif action == '-':
        res = number_1 - number_2
        print(res)
    elif action == '*':
        res = number_1 * number_2
        print(res)