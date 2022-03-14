a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

def division(a=a, b=b):
    result = a / b
    print(f'{a}/{b}={result}')

if b == 0:
    print('Can't divide by zero!')
else:
    division()
