"""
Exercise 3.11

The program should:

ask the user for 5 numeric data
verify that they are integers and if not, ask for the 5 again
when the 5 data are available, the program should return the average
no errors should appear.
"""

flag = True
while flag:
    try:
        a = (input("Enter first integer: "))
        while not a.isnumeric():
            print("Enter other datum")
            a = (input("Enter first integer: "))
        a = int(a)
        b = (input("Enter second integer: "))
        while not b.isnumeric():
            print("Enter another datum")
            b = (input("Enter second integer: "))
        b = int(b)
        c = (input("Enter third integer: "))
        while not c.isnumeric():
            print("Insert another datum")
            c = (input("Enter third integer: "))
        c = int(c)
        d = (input("Enter forth integer: "))
        while not d.isnumeric():
            print("Insert other data")
            d = (input("Enter forth integer: "))
        d = int(d)
        f = (input("Insert fifth integer: "))
        while not f.isnumeric():
            print("Insert other data")
            f = (input("Enter fifth integer: "))
        f = int(f)
        addition = a + b + c + d + f
        prom = (addition/5)
        print(f"Promedy is: {prom}")
        flag = False
    except ValueError as e:
        print(f"Error: {e}")
    out = input("Wish to finish process?")
    if out.lower == "yes":
        flag = False
