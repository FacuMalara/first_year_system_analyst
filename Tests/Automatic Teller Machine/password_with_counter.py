# exercise 3.14
balance = 50000


def system_entry():
    counter = 0
    pin = 1234
    flag = True
    while flag:
        try:
            print("enter your PIN")
            entered_pin = int(input(""))
            if entered_pin != pin:
                print("incorrect PIN")
                counter += 1
            if counter == 3:
                print(
                    "access has been blocked for security, you have exhausted 3 attempts")
                flag = False
                print("you have exited")
                return flag
            elif entered_pin == pin:
                print("the PIN is correct")
                return flag
        except:
            print("something went wrong, verify that the PIN is numeric")


def display_menu():
    print("""
                 1- check balance
                 2- deposit money
                 3- withdraw money
                 4- Exit """)


def show_balance():
    global balance
    print(f"your balance is ${balance}")


def deposit_money():
    global balance
    print("how much money do you want to deposit?")
    try:
        money = int(input())
        balance = balance + money
        print(f"your balance is $ {balance}")
    except:
        print("You entered something wrong")


def withdraw_money():
    global balance
    print("how much money do you want to withdraw?")
    try:
        withdraw = int(input())
        if withdraw > balance:
            print(f"insufficient balance, enter an amount less than {balance}")
        else:
            balance = balance - withdraw
            print(f"your balance is ${balance}")
    except:
        print("Entered non-numeric character")
