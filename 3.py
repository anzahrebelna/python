class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = input('Введите число и нажимайте Enter, для выхода впишите Stop: ')
                int_val = int(val)
                self.my_list.append(int_val)
                print(f'{self.my_list} \n ')
            except:
                if val == 'Stop':
                    return f'Вы вышли'
                    break
                else:
                    print(f"Недопустимое значение")



try_except = Error(1)
print(try_except.my_input())