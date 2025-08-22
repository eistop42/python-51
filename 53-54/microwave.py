class Microwave():
    def __init__(self):
        self.timer = 0
        self.power = 0

    def set_mic_power(self, user_power):
        if 0 < user_power <= 600:
            self.power = user_power
        else:
            print('Недопустимая мощность')

    def set_mic_time(self, user_time):
        if 0 < user_time <= 30:
            self.timer = user_time
        else:
            print('Недопустимое время')

    def heat(self):
        # условие на проверку таймера и мощности
        print(f'Греем...Мощность {self.power} Время {self.timer}')

mic = Microwave()
mic.set_mic_time(10)
mic.set_mic_power(300)
mic.set_mic_power(1000)
mic.heat()