from sys import argv

def salary():
    try:
        time, rate, bonus - map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("print 3 numbers.")

salary()

