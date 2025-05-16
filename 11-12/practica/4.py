all_sum = 0
for i in range(2):
    count = int(input('кол-во: '))
    price = float(input('цена: '))
    if count >0 and price >0:
        sum = count * price
        all_sum = all_sum + sum
        print(sum)
    else:
        print('невалидные данные')

print(all_sum)