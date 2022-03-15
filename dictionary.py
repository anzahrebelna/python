month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
num_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_dictionary = dict(zip(num_month, month))

num = int(input('Enter month number: '))

if num < 13:
    print(f"{num} month of year is {month_dictionary.get(num)}.")
else:
    print('There are only 12 months in a year!')
