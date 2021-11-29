month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
num_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_dictionary = dict(zip(num_month, month))

num = int(input('Введите номер месяца: '))

if num < 13:
    print(f"{num} месяц года - это {month_dictionary.get(num)}.")
else:
    print('В году всего 12 месяцев!')