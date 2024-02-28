"""
###Exercise 4.1 (Calculator)
The program should:

Have 4 functions (addition, subtraction, division, and multiplication)
Have a menu where it should ask the user which operation to perform
Ask for the two numbers to operate and return the result to the user
Handle possible errors"""


def addition(a, b):
    try:
        oper_addition = float(a)+float(b)
        print(f"the addition {a} + {b} is: {oper_addition}")
    except ValueError as e:
        print(f"bad arguments {e}")


def substraction(a, b):
    try:
        oper_substraction = float(a)-float(b)
        print(f"substraction {a} - {b} is: {oper_substraction}")
    except ValueError as e:
        print(f"bad arguments {e}")


def multiplication(a, b):
    try:
        mult = float(a)*float(b)
        print(f"multiplication {a} * {b} is: {mult}")
    except ValueError as e:
        print(f"bad arguments {e}")


def division(a, b):
    try:
        oper_div = float(a)/float(b)
        print(f" division {a} / {b} is: {oper_div}")
    except ValueError as e:
        print(f"bad arguments {e}")


def ask_for_two_floats(text_1, text_2):
    while True:
        try:
            num_1 = float(input(text_1))
            num_2 = float(input(text_2))
            return num_1, num_2
        except ValueError as e:
            print(f'Arguments must be decimal {e}')


def main():
    while True:
        menu = """
        CALCULATOR
        1.   Add
        2.   Substract
        3.   Multiply
        4.   Divide
        5.   Out

        option: """

        option = input(menu)
        if option in ['1', '2', '3', '4']:
            a, b = ask_for_two_floats(
                'Give me a number: ', 'Give me a number: ')
        match option:
            case '1':
                addition(a, b)
            case '2':
                substraction(a, b)
            case '3':
                multiplication(a, b)
            case '4':
                division(a, b)
            case '5':
                print('Ending process')
                return
            case _:
                print('incorrect option')


if __name__ == "__main__":
    main()
