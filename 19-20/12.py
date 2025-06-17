from random import randint
n = int(input('Укажи количество чисел в массиве: '))
mas = []
for i in range(1, n+1):
    # s = int(input(f'Введи {i} из {n} число: '))
    s = randint(-100,100)
    mas.append(s)
max1 = mas[0]
min1 = mas[0]
for num in mas:
    if num > max1:
        max1 = num
    if num < min1:
        min1 = num
print(mas)
print(f'Максимальная разница значений {min1} и {max1} составляет {abs(abs(min1) - abs(max1))}')