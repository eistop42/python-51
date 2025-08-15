
class RedButton():

    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1
        print('Тревога!')

    def count(self):
        return self.clicks

first_button = RedButton()
first_button.click()
first_button.click()
first_button.click()
print(first_button.count())
