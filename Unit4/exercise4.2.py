"""
###Exercise 4.2 (Measurements)
The program should:

Have 4 functions (calculate Area (square), calculate Perimeter (square), calculate Area (circle), calculate Perimeter (circle))
Have a menu where it should ask the user which operation to perform
Ask for the two parameters and return the result to the user
Handle possible errors
"""
# missing units of measurement
import math


def calculate_square_area(base, hight):
    return base*hight


def calculate_square_perimeter(base, hight):
    return 2 * base + 2 * hight


def calculate_circle_area(radius):
    return math.pi * math.pow(radius, 2)


def calculate_circle_perimeter(radius):
    return 2*math.pi*radius


def ask_two_sides():
    while True:
        try:
            side1 = float(input("Give me first side: "))
            side2 = float(input("Give me second side: "))
            return side1, side2
        except ValueError as e:
            print(f'Arguments must be integer or decimal {e}')


def ask_radius():
    while True:
        try:
            radius = float(input("Give me circle radius: "))
            return radius
        except ValueError as e:
            print(f'Arguments must be integer or decimal {e}')


def main():
    while True:
        menu = """
        
        Measurements
    1. Calculate the area of a quadrilateral
    2. Calculate the perimeter of a quadrilateral
    3. Calculate the area of a circle
    4. Calculate the perimeter of a circle
    5. Exit

Option: """

        option = input(menu)
        match option:
            case '1':
                side1, side2 = ask_two_sides()
                print(calculate_square_area(side1, side2))
            case '2':
                side1, side2 = ask_two_sides()
                print(calculate_square_perimeter(side1, side2))
            case '3':
                radius = ask_radius()
                print(calculate_circle_area(radius))
            case '4':
                radius = ask_radius()
                print(calculate_circle_perimeter(radius))
            case '5':
                print('Out')
                return
            case _:
                print('Incorrect option')


if __name__ == "__main__":
    main()
