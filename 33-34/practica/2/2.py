import json

products = []

for i in range(4):
    name = input('название товара: ')
    price = input('цена товара: ')

    prod = {'name': name, 'price': price}
    products.append(prod)

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)
