# Пример вызова:
rub_amount = float(input("Введите сумму в рублях: "))  # 1000
currency = input("Введите валюту (USD, EUR, CNY): ")   # USD


def convert_currency(rub_amount, currency):
    if currency == 'USD':
        return rub_amount / 100
    elif currency == 'EUR':
        return rub_amount / 120

converted = convert_currency(rub_amount, currency)
print(f"{rub_amount} рублей = {converted} {currency}")  # 1000 рублей = 11.0 USD