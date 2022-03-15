rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('task4.txt', 'r') as file_obj:
     content = file_obj.readlines()
     for i in content:
         i = i.split(' ')
         print(i[2])
         new_file.append(rus.pop(i[0]) + ' - ' + i[2])
     print(new_file)

with open('task4_new.txt', 'w') as file_obj_2:
     file_obj_2.writelines(new_file)
