order_cost = 0
discount = 10
amount_tickets = int(input('Сколько билетов Вам необходимо? '))

for ticket in range(amount_tickets):
    ticket += 1
    age_visitors = int(input(f'Для какого возраста билет №{ticket}? '))
    if age_visitors < 18:
        print('Сегодня детям бесплатно!')
    elif 18 <= age_visitors < 25:
        order_cost += 990
        print('Стоимость билета: 990 ₽.')
    else:
        order_cost += 1390
        print('Стоимость билета: 1390 ₽.')
if amount_tickets > 3:
    order_cost = order_cost - ((order_cost / 100) * discount)
    print(f'Поздравляю! Вы получаете скидку 10% за количество участников. Сумма к оплате {round(order_cost,2)} ₽.')
else:
    print(f'Итоговая сумма к оплате {order_cost} ₽.')
