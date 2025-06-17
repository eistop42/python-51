numbers = [43, 5, -1, 4, 12, -4]
count = 0
sum = 0

count_p = 0
sum_p = 0
for number in numbers:
    if number > 0:
        count_p += 1
        sum_p += number
    count += 1
    sum += number

print(f'Среднее всех чисел: {sum/count}')
print(f'Среднее всех полож. чисел: {sum_p/count_p}')