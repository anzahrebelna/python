lines = 0
with open('task1.txt', 'r') as f:
    for line in f:
        lines = lines + 1
    print(f'Количество строк - {lines}')

with open('task1.txt', 'r') as f:
    i = 1
    while i <= lines:
        content = f.readline()
        content = content.split('_')
        print(f'В {i}-ой строке - {len(content)} слов.')
        i += 1

