# ООП стиль

class Calculator:

    def __init__(self):
        # создание атрибутов по умолчанию
        self.operations = 0
        self.limit = 2
        self.name = ''

    def sum(self, a, b):
        """Метод для сложения"""
        print(self.check_limit())
        if  self.check_limit() == False:
            self.operations += 1
            return a + b
        return 'Операции истекли'

    def minus(self, a, b):
        """Метод для вычитания"""
        if self.check_limit() == False:
            self.operations += 1
            return a - b
        return 'Операции истекли'

    def multi(self, a, b):
        """Метод для умножения"""
        self.operations += 1
        return a * b

    def check_limit(self):
        """Проверка лимита на операции"""
        if self.operations >= self.limit:
            return True
        return False


# создание объекта класса Calculator
my_calc = Calculator()
print(my_calc.operations)

while True:
    number_1 = int(input('Первое число: '))
    number_2 = int(input('Второе число: '))
    action = input('Дествие: +-*/: ')

    if action == '+':
        res = my_calc.sum(number_1, number_2)
    elif action == '-':
        res = my_calc.minus(number_1, number_2)
    elif action == '*':
        res = my_calc.multi(number_1, number_2)
    print(my_calc.operations)
    print(res)