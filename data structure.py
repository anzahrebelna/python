print('Goods: ')
name1 = input('Name of the first item:')
name2 = input('Name of the second item:')
name3 = input('Name of the third item:')
price1 = input('Price of the first item:')
price2 = input('Price of the second item:')
price3 = input('Price of the third item:')
amount1 = input('Quantity of the first item:')
amount2 = input('Quantity of the second item:')
amount3 = input('Quantity of the third item:')
unit1 = input('Unit of the first item:')
unit2 = input('Unit of the second item:')
unit3 = input('Unit of the third item:')

#1
article1 = (name1, price1, amount1, unit1)
article2 = (name2, price2, amount2, unit2)
article3 = (name3, price3, amount3, unit3)
article = ('Name', 'Price', 'Quantity', 'Unit')

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
