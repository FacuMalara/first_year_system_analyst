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
Help (how to compare strings and integers, be careful 
with casting before checking if the user entered str or int)

"""

print("Menu:\n\n1.Option 1\n2.Option 2\n3.Option 3")

while True:
    try:
        menu = int(input("Insert menu option '1' '2' o '3': "))
        match menu:
            case 1:
                print(menu)
            case 2:
                print(menu)
            case 3:
                print(menu)
                break
            case _:
                print("Error")
    except ValueError as e:
        print("ERROR")
