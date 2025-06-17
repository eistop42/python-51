import random
q = random.randint(1,3)
w = 0
for i in range(3):
    namber = int(input('Введите число от 1 до 10  '))
    if q == namber:
        print(f'Ты угадал c {w+1} попытки')
        break
    else:
        w += 1
        print(f'Не угадал, повтори попытку')
else:
    print(f'Ты не угадал, загаданое число {q}')