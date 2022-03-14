result = int(input('Enter initial result:'))
expect_result = int(input('Enter expected result:'))
count = 1

while result < expect_result:
    result = result + result * 0.1
    count = count + 1

print(count)
