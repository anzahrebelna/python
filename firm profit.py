earnings = int(input('Enter revenue value:'))
costs = int(input('Enter cost value:'))

profit = earnings - costs# profit

if profit > 0:
    print('Your firm is profitable!')
else:
    print('Your company is operating at a loss.')

if profit > 0:
    employee = int(input('Enter the number of employees:'))
    profitability = profit / earnings * 100
    print('Your company's return on revenue is:', profitability, '%')
    profit_per_employee = profit / employee
    print('Profit per employee is:', profit_per_employee)
