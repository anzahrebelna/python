def my_func(x,y):
    n = abs(y)
    result = x
    while n > 1:
        result = result * x
        n = n - 1

    result = 1 / result
    print(result)

my_func(1,-4)
