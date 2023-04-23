deposit = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Сумма вашего вклада: '))
deposit.append(money * per_cent['ТКБ'] / 100)
deposit.append(money * per_cent['СКБ'] / 100)
deposit.append(money * per_cent['ВТБ'] / 100)
deposit.append(money * per_cent['СБЕР'] / 100)
print('Годовой процент накоплений в каждом из банков =', list(map(int, deposit)))
print('Максимальная сумма, которую вы можете заработать —', int(max(deposit)))