"""
Exercise 5.6 (Greengrocer's Inventory Program)
Create a program that should:

Have a stock of fruits and another one of vegetables 
(The stock indicates if they sell that fruit or vegetable or not,
 not the quantity) - use lists within lists

Have a menu and 3 functions

1. Add fruits or vegetables to the corresponding stock 
    (checking if they are new)
2. Check the stock of fruits or vegetabl
"""
from functions import *
from stock_frutas import *


def main():
    test = [["Fruits"], ["Stock"]]
    while True:
        manu = input("""
Menu:

1. Add a fruit
2. Check if a fruit is in stock
3. Remove a fruit from stock
4. Remove units of a fruit
5. Show list of fruits and stock
6. Exit
                     
Enter option:  """)

        match manu:
            case "1":
                test = add_fruit(test)
            case "2":
                consult_stock(test)
            case "3":
                test = delete_fruit(test)
            case "4":
                test = discount_units(test)

            case _:
                print("Invalid data entered")


if __name__ == "__main__":
    main()
