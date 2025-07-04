# Пример вызова:
password1 = input("Введите первый пароль: ")  # qwerty123
password2 = input("Введите второй пароль: ")  # qwerty123

def check_passwords(pass1, pass2):
    if pass1 == pass2:
        return True
    else:
        return False

result = check_passwords(password1, password2)
print(result)  # True