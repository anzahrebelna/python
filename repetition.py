data = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_data = [el for el in data if data.count(el) < 2]
print(new_data)
