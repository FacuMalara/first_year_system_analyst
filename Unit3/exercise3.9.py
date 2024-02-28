"""
Exercise 3.9
The program should:

Ask the user for an initial number
Ask the user for a limit number
print from the initial to the limit
should not generate errors
"""
flag = True
while flag:
    try:
        start = int(
            input("Enter initial number, it must be less than the limit: "))
        limit = int(input("Enter limit number: "))
        while limit > start:
            flag = False
            start += 1
            print(limit)
        if flag:
            print("Insert other numbers")
    except ValueError as e:
        print("Error")

print("Out off while loop")
