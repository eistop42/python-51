import os
from datetime import datetime
class Calc():
    def add(self, number_1, number_2):
        res = number_1 + number_2
        print(res)
        self.log(number_1, number_2, res, 'сложение')

    def subtract(self, number_1, number_2):
        res = number_1 - number_2
        print(res)
        self.log(number_1, number_2, res, 'вычитание')

    def _log(self, number_1, number_2, res, action):
        """Запись действий в файл"""
        if os.path.exists('log.txt'):
            open_mode = 'a'
        else:
            open_mode = 'w'
        with open('log.txt', open_mode, encoding='utf-8') as f:
            data = f'{datetime.now()}: {number_1} {action} {number_2} = {res}\n'
            f.write(data)


calc = Calc()
calc.add(3, 4)
calc.subtract(3, 4)