print('Товары: ')
name1 = input('Название первого товара:')
name2 = input('Название второго товара:')
name3 = input('Название третьего товара:')
price1 = input('Цена первого товара:')
price2 = input('Цена второго товара:')
price3 = input('Цена третьего товара:')
amount1 = input('Количество первого товара:')
amount2 = input('Количество второго товара:')
amount3 = input('Количество третьего товара:')
unit1 = input('Единица первого товара:')
unit2 = input('Единица второго товара:')
unit3 = input('Единица третьего товара:')

#1
article1 = (name1, price1, amount1, unit1)
article2 = (name2, price2, amount2, unit2)
article3 = (name3, price3, amount3, unit3)
article = ('Название', 'Цена', 'Количество', 'Ед.')

dictionary1_1 = dict(zip(article, article1))
dictionary1_2 = dict(zip(article, article2))
dictionary1_3 = dict(zip(article, article3))

turple1 = (1, dictionary1_1)
turple2 = (2, dictionary1_2)
turple3 = (3, dictionary1_3)

articles = [turple1, turple2, turple3]
print(articles)

#2
names = [name1, name2, name3]
prices = [price1, price2, price3]
amounts = [amount1, amount2, amount3]
units = [unit1, unit2, unit3]
parametrs = (names, prices, amounts, units)
dictionary_main = dict(zip(article, parametrs))

print(dictionary_main)
