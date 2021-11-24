result = int(input('Введите начальный результат:'))
expect_result = int(input('Введите ожидаемый результат:'))
count = 1

while result < expect_result:
    result = result + result * 0.1
    count = count + 1

print(count)
