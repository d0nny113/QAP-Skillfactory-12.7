per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму депозита:"))
deposit = list(per_cent.values())
for i in range(len(deposit)):
    deposit[i] = money / 100 * deposit[i]
depositMax = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать -", depositMax)
