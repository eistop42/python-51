

class Programmer():
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.zp = 0
        self.hours = 0

    def info(self):
        return f'{self.name} {self.hours}ч. {self.zp}тгр.'

    def work(self, hours):
        "Поситать зп, добавить к общим показателям часы и сумму"
        # посчитать зп



programmer = Programmer('Васильев Иван', 'Junior')
print(programmer.info())