secret = 6

for i in range (3):
    user = int(input('Введите число от 1 до 10: '))
    if user == secret:
        print('угадал')
        break
    else:
        print('не угадал')
