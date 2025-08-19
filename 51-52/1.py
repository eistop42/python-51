class Lamp():
    def __init__(self, color, lamp=None):
        self.status = False
        self.level = 0
        self.color = color
        self.lamp = lamp

    def show(self):
        """Посмотреть статус лампочки"""
        print('Статус: ', self.status)

    def turnOn(self):
        """Включить лампочку"""
        self.status = True
    def turnOf(self):
        """Выключить лампочку"""
        self.status = False

    def raise_level(self):
        if self.level < 10:
            self.level += 1
        print('Яркость', self.level)

    def low_level(self):
        if self.level >0:
            self.level -= 1
        elif self.level == 0:
            self.turnOf()
        print('Яркость', self.level)

l1 = Lamp('зеленая')
l2 = Lamp('красная', l1)

l1.turnOn()
