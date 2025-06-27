import json

with open('products.json', encoding='utf-8') as f:
    products = json.load(f)

# недоделанный код!!!!!!
while True:
    print('1- добавить товар, 2 - посмотреть')
    choice = input('выбери действие: ')
    if choice == '1':
        name = input('название: ')
        price = input('цена: ')
        find = False
        for prod in products:
            if prod['name'] == name:
                find = True
        if not find:
            prod = {'name': name, 'price': price}
            products.append(prod)
        else:
            print('такое есть')
        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False)

    if choice == '2':
        print(products)