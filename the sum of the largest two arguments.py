a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

def sum_of_two(a=a,b=b,c=c):
    our_list = [a, b, c]
    sorted_list = sorted(our_list)
    result = sum(our_list[1::])
    print(f'the sum of the largest two arguments is - {result}')

sum_of_two()
