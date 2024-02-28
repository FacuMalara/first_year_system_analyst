"""
Exercise 5.6 (Greengrocer Inventory Program)
Create a program that should:

Have a stock of fruits and vegetables (The stock indicates whether they sell that fruit or vegetable or not, not the quantity) - use lists inside lists.

Have a menu and 3 functions:

Add fruits or vegetables to the corresponding stock (checking that they are new).
Check the stock of fruits or vegetables.
Delete an item from the stock.
"""

from functions import *


def menu():
    list_of_fruits = [["fruits"], ["stock"]]

    while True:

        option = input(
            """Options Menu
1. Add fruits or vegetables
2. Check stock
3. Delete an item
4. Subtract units
5. Add units
6. Exit

Enter an option: """)

        match option:
            case "1":
                list_of_fruits = add_fruits(list_of_fruits)
            case "2":
                consult_stock(list_of_fruits)
            case "3":
                list_of_fruits = delete_fruit(list_of_fruits)
            case "4":
                list_of_fruits = discount_units(list_of_fruits)
            case "5":
                list_of_fruits = add_stock(list_of_fruits)
            case "6":
                print("Finish process")
                return


if __name__ == "__main__":
    menu()
