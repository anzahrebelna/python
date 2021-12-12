poor = []
salary = []
with open('task3.txt', 'r') as my_file:
    content = my_file.readlines()
    for i in content:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])
    print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, salary)) / len(salary)}')
