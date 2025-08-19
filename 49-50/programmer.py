
# Junior — с окладом 10 тугриков в час;
# ● Middle — с окладом 15 тугриков в час;
# ● Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за

class Programmer():
    oklad = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.zp = 0
        self.hours = 0
        self.bonus = 0
        self.senior_rise = 1

    def info(self):
        return f'{self.name} {self.hours}ч. {self.zp}тгр.'

    def work(self, hours):
        "Поситать зп, добавить к общим показателям часы и сумму"
        # посчитать зп
        self.hours += hours
        self.zp += (self.oklad[self.grade] + self.bonus) * hours
    def rise(self):
        if self.grade == 'Junior':
            self.grade = 'Middle'
        elif self.grade == 'Middle':
            self.grade = 'Senior'
        elif self.grade == 'Senior':
            self.bonus += self.senior_rise


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())