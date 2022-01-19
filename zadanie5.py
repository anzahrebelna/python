earnings = int(input('Введите значение выручки:'))
costs = int(input('Введите значение издержек:'))

profit = earnings - costs# прибыль

if profit > 0:
    print('Ваша фирма приносит прибыль!')
else:
    print('Ваша фирма работает в убыток.')

if profit > 0:
    employee = int(input('Введите число сотрудников:'))
    profitability = profit / earnings * 100
    print('Рентабельность выручки Вашей фирмы составляет:', profitability, '%')
    profit_per_employee = profit / employee
    print('Прибыль на одного работника составляет:', profit_per_employee)
