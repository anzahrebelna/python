a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def division(a=a, b=b):
    result = a / b
    print(f'{a}/{b}={result}')

if b == 0:
    print('Делить на ноль нельзя!')
else:
    division()
