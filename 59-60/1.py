class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_info(self):
        print(f'Инфо: {self.name} {self.__age}')

u1 = User('Алиса', 42)
u1.get_info()
print(u1._User__age)