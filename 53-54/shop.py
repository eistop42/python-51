class Shop:

    def __init__(self):
        self.all_sum = 0
        self.count_products = 0
        self.products = [{'name': 'Хлеб', 'price': 50, 'count': 2},
                         {'name': 'Молоко', 'price': 60, 'count': 1}]

    def buy(self, product_name, shop):
        # ищем продукт по имнеи
        for product in self.products:
            if product['name'] == product_name:
                if product['count'] > 0:
                    print(f'Купили: {product_name} ')
                    self.all_sum += product['price']
                    self.count_products += 1
                    product['count'] -= 1
                else:
                    print('товар закончился...')
                break
        else:
            print('такого товара нет')

    def add_products(self, name, price, count=1):
        product = {'name': name, 'price': price, 'count': count}
        self.products.append(product)
        print(f'Добавили товар: {name}')

    def get_info(self):
        print(f'Сумма всех покупок: {self.all_sum} Количество: {self.count_products}')


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


shop = Shop()
shop.buy('Молоко')
shop.buy('Молоко')
shop.add_products('Сок', 200, 2)
shop.buy('Сок')
shop.get_info()