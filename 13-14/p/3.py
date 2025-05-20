numbers = [12, 4, 5, -3, 12, -6, 1, 7, 2]
sum1 = 0
sum2 = 0
sum3 = 1

for i in range(len(numbers)):
    if numbers[i] < 0:
        sum1 += numbers[i]
    if numbers[i] % 2 == 0:
        sum2 += numbers[i]
    if i % 3 == 0:
        sum3 *= numbers[i]

print('Отрицательные: ', sum1)
print('Четные: ', sum2)
print('Произведение кратных 3: ', sum3)