my_list = [7, 5, 3, 3, 2]

new_num = int((input('Enter a number:')))
my_list.append(new_num)

sorted_list = sorted(my_list)
print(sorted_list[::-1])
