from random import randint
with open('task5.txt', 'w+') as f:
    f.write(" ".join([str(randint(1,100)) for _ in range(1000)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))
