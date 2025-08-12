
class Cat:
    def __init__(self, name, color):
        self.cat_name = name
        self.cat_color = color
        self.age = 0
        self.mood = 50

    def meow(self):
        print(f'Мяу, я {self.cat_name}')

    def eat(self):
        print('Я поел')
        self.mood += 10
        print('Мое настроение', self.mood)

cat1 = Cat('Барсик', 'рыжий')
cat2 = Cat('Мурзик', 'белый')

cat1.meow()
cat2.meow()
cat2.eat()