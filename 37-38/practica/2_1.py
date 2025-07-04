# Пример вызова:
rub_amount = float(input("Введите сумму в рублях: "))  # 1000
currency = input("Введите валюту (USD, EUR, CNY): ")   # USD

curr = {'USD': 100, 'EUR': 120}
def convert_currency(rub_amount, currency):
    if currency in curr:
        res = rub_amount / curr[currency]
        return res

converted = convert_currency(rub_amount, currency)
print(f"{rub_amount} рублей = {converted} {currency}")  # 1000 рублей = 11.0 USD