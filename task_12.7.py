per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

print("Введите сумму вклада")
money = int(input())

interest_rates = list(per_cent.values())

deposit = []
for rate in interest_rates:
    deposit.append(rate * money / 100)

best_option = max(deposit)

print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать — ", best_option)
