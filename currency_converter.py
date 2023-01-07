#!/usr/bin/env python
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

c = CurrencyRates()
currency_codes = CurrencyCodes()
currencies = list(c.get_rates('USD').keys())

print(
        "1. Get the exchange rate between two currencies\n"
        "2. Convert some money from a currency to another\n"
        "What do you want to do? (Enter the number, 1 or 2): ",
        end=""
        )
operation = input()


counter = 1
print(str(counter) + ". USD" + " - " + currency_codes.get_currency_name('USD'))
for currency in currencies:
    counter += 1
    print(str(counter) + ". " + currency + " - " + currency_codes.get_currency_name(currency))

print("Select your base currency (Enter the number e.g. 1, 5, 12, etc.): ", end="")
base_cur = int(input())

print("Select your destination currency (Enter the number e.g. 1, 5, 12, etc.): ", end="")
dest_cur = int(input())

if base_cur == 1:
    base_cur = 'USD'
else:
    base_cur = currencies[base_cur - 2]


if dest_cur == 1:
    dest_cur = 'USD'
else:
    dest_cur = currencies[dest_cur - 2]


if operation == '1':
    print("1 " + currency_codes.get_symbol(base_cur) + " = " + str(c.get_rate(base_cur, dest_cur)) + " " + currency_codes.get_symbol(dest_cur))
elif operation == '2':
    print("Enter your money amount as an integer (e.g. 10, 132, etc.): ", end="")
    amount = int(input())
    print(str(amount) + " " + currency_codes.get_symbol(base_cur) + " = " + str(c.convert(base_cur, dest_cur, amount)) + " " + currency_codes.get_symbol(dest_cur))
