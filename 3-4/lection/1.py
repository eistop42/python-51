balance = 500
price = 600
money_mode = False

money_code = '123'
code = input('Введи код для денег: ')
if code == money_code:
    money_mode = True

if balance >= price or money_mode == True:
    balance -= price
    print(f'Купили товар, остаток: {balance}')
else:
    print('Не хватает денег')