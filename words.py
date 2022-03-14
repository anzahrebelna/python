def int_func(word):
    latinletter = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latinletter) else False

words = input('fff: ').split()
for el in words:
    result = int_func(el)
    if result:
        print(int_func(el), ' ')
