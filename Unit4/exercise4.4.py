"""
Exercise 4.4 (Unit Converter)
The program should:

Have 4 functions:
Celsius to Fahrenheit converter (temperature in °C).(look up the formula)
cm3 to liters converter (quantity in cm3)
liters to cm3 converter (quantity in liters)
Pesos to Dollars converter (pesos)
Have a menu where it should ask the user which operation to perform
Ask for the parameters and return the result to the user
Handle possible errors
"""


def fahr(degrees_cel):
    try:
        degrees_fahr = degrees_cel * (9/5) + 32
        print(degrees_fahr)
    except ValueError as e:
        print(f"Invalid enter {e}")


def liters_(cm3):
    try:
        liters = cm3/1000
        print(liters)
    except ValueError as e:
        print(f"Invalid income {e}")


def liters_to_cm3(liters):
    try:
        centimeters3 = liters * 1000
        print(centimeters3)
    except ValueError as e:
        print(f"Invalid income {e}")


def dolar(pesos):
    try:
        dolares = pesos/725
        print(dolares)
    except ValueError as e:
        print(f"Invalid income {e}")


def ask_datum(text_1):
    while True:
        try:
            num = float(input(text_1))
            return num
        except ValueError as e:
            print(f"Invalid datum {e}")


def main():
    while True:
        menu = """
                 UNIT CONVERTER
1. Celsius to Fahrenheit converter
2. cm3 to liters converter
3. liters to cm3 converter
4. Pesos to Dollars converter
5. Exit

markdown
Copy code
            Option: 
                """
        try:
            option = input(menu)
            if option == "1" or option == "2" or option == "3" or option == "4":
                num = ask_datum("Enter number: ")
            match option:
                case "1":
                    fahr(num)
                case "2":
                    liters_(num)
                case "3":
                    liters_to_cm3(num)
                case "4":
                    dolar(num)
                case "5":
                    print("Ending process")
                    return
                case _:
                    print("Invalid")
        except ValueError as e:
            print(f"Non computable data entered {e}")


if __name__ == "__main__":
    main()
