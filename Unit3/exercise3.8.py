"""
Exercise 3.9
The program should:

Ask the user for an initial number
Ask the user for a limit number
print from the initial to the limit
should not generate errors
"""
try:
    num_in = int(input("Insert integer number: "))
    num_lim = int(input("Insert limit number: "))
    if num_in <= num_lim:
        while num_in <= num_lim:
            print(num_in)
            num_in += 1
    elif num_in >= num_lim:
        while num_in >= num_lim:
            print(num_in)
            num_in -= 1

except ValueError as e:
    print(f"Invalid: {e}")
