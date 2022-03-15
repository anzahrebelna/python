class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = input('Enter a number and press Enter, to exit, type Stop: ')
                int_val = int(val)
                self.my_list.append(int_val)
                print(f'{self.my_list} \n ')
            except:
                if val == 'Stop':
                    return f'You got out'
                    break
                else:
                    print(f"Invalid value")



try_except = Error(1)
print(try_except.my_input())
