"""
Exercise 5.6 (Greengrocer's Inventory Program)
Create a program that should:

Have a stock of fruits and another one of vegetables 
    (The stock indicates if they sell that fruit or vegetable or 
    not, not the quantity) - use lists within lists

Have a menu and 3 functions

1. Add fruits or vegetables to the corresponding stock (checking 
    if they are new)
2. Check the stock of fruits or vegetables
3. Remove an item from the stock
"""
from functions import *


def menu(base_fruits):
    while True:
        menu = """
1.  Add fruits
2.  Check fruit stock
3.  Remove an item from the stock
4.  List table
5.  Remove an amount from a stock
6.  Exit

Option:"""
        option = input(menu)
        match option:
            case '1':
                base_frutas = add_stock(base_fruits)
            case '2':
                consult_stock(base_fruits)
            case '3':
                base_frutas = delete_stock(base_fruits)
            case '4':
                print_base(base_frutas)
            case '5':
                base_frutas = descount_stock(base_fruits)
            case '6':
                print('Ending process')
                return
            case _:
                print('Incorrect option')


if __name__ == "__main__":
    menu(base_fruits)
