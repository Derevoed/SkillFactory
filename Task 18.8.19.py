n = int(input('Укажите количество билетов: '))
age = [int(input('Укажите возраст каждого посетителя: ')) for i in range(n)]
total = 0
for person in age:
    if 18 <= person < 25:
        total += 990
    elif person >= 25:
        total += 1390
if n > 3:
    print('Стоимость билетов с учетом скидки в 10%:', int(total * 0.9), 'руб.')
else:
    print('Полная стоимость билетов:', total, 'руб.')