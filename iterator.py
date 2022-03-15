from itertools import count, cycle

for el in count(int(input('Введите число: '))):
    if el == 20:
        break
    print(el)


my_list = [False, 'nanana', 666, True, None]
for el in cycle(my_list):
    print(el)
