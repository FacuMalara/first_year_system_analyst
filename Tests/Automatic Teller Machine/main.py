# ATM entry
from password_with_counter import *

# entry = system_entry

# I removed a balance you put above this comment, it was not necessary because you defined it in the other file
# you were missing the system entry, it entered directly into the menu
# it goes through the menu function and gets stuck because you put an input in a statement
# I recommend that you include some code to avoid this
access = system_entry()
if access:
    print("Welcome, enter the desired option")
    display_menu()
    flag = True
    while flag:
        # get used to working with try, except. The code produces an error if you enter a character that is not numeric
        try:
            option = int(input())
            match option:
                case 1:
                    show_balance()
                case 2:
                    deposit_money()
                case 3:
                    withdraw_money()
                case 4:
                    print("Exiting")
                    flag = False
                    break
                    # if you don't put a break here, the code will continue to execute and will print the print statement below
                    # you never changed the boolean value of the flag
            print("Do you want to perform another operation?")
        except:
            print("Entered non-numeric character")
