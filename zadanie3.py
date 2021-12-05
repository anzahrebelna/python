a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

def sum_of_two(a=a,b=b,c=c):
    our_list = [a, b, c]
    sorted_list = sorted(our_list)
    result = sum(our_list[1::])
    print(f'Сумма наибольших двух аргументов - {result}')

sum_of_two()
