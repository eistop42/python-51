def sum(a, b):
    return a+b

def raznost(a, b):
    return a-b


while True:
    number_1 = int(input('первое число: '))
    number_2 = int(input('второе число: '))
    action = input('Выбирай 1 - сложить, 2 - вычеcть')

    if action == '1':
        print(sum(number_1, number_2))
        # вызвать функцию сложения
    elif action == '2':
        print(raznost(number_1, number_2))
