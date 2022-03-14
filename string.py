str = (input()).split('Enter the string: ')

for ind, el in enumerate(str, 1):
    if len(el) > 10:
        print(ind, el[:10])
    else:
        print(ind, el)

