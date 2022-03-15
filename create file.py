with open("task1.txt", "w+") as f1:
    line = input('Введите строку: ')
    while line:
        f1.write(f'{line} \n')
        line = input('Введите строку: ')
        if not line:
            break

    f1.seek(0)
    context = f1.readlines()
    print(context)
