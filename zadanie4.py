your_number = int(input('Введите целое положительное число:'))
max_number = 0

while your_number > 0:
    if your_number % 10 > max_number:
        max_number = your_number % 10
    your_number = your_number // 10

print(max_number)
