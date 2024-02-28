"""
Exercise 3.7:
The program should:

Display a menu to the user
Allow the user to enter a menu option
print that option
if no menu option is entered, indicate ERROR
Conditions:

print (string)
1 (int)
2 (int)
exit (string)
Help (how to compare strings and integers, be careful with 
casting before checking if the user entered str or int)
"""

print("Welcome, you will now be shown a couple of options,\nenter the one you desire\n1. Option 1\n2. Option 2\n3. Exit")

while True:
    menu = input("Insert '1' '2' o '3': ")
    if menu.isnumeric():
        menu = int(menu)
        if menu == 1:
            print(menu)
        elif menu == 2:
            print(menu)
        elif menu == 3:
            print(menu)
            break
        else:
            print("Error")
    else:
        print("ERROR")
