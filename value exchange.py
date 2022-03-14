numbers = list(input('Enter string/number: '))
if len(numbers) % 2 == 0:
    numbers[::2], numbers[1::2] = numbers[1::2], numbers[::2]
else:
    numbers[:-1:2], numbers[1::2] = numbers[1::2], numbers[:-1:2]
print(' '.join([str(i) for i in numbers]))
