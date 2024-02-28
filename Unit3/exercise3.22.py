"""
Exercise 3.22
The program should:

Ask the user for the number of people
ask the user one by one for the age of the people
once the ages are loaded, it should print the oldest age on the screen
should not generate errors
"""

flag = True
while flag:
    try:
        amount_people = int(input("Enter number of persons: "))
        bigger_age = 0
        for i in range(amount_people):
            age = int(input(f"Enter persons age {i+1}:"))
            if bigger_age < age:
                bigger_age = age
        print(f"Bigger age is {bigger_age}")
    except ValueError as e:
        print("Invalid datum")
    out = input("Wish to end process? y o n: ")
    if out == "y":
        break
