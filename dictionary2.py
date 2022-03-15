import re
patter = re.compile('[0-9]+')
content = {}
with open('task6.txt', 'r') as f:
    for line in f:
        name, hours = line.split(':')
        elems = [i for i in hours if i == ' ' or (i >= '0' and i <= '9')]
        print(elems)
        name_sum = sum(map(int, "".join(elems).split()))
        content[name] = name_sum

print(content)

