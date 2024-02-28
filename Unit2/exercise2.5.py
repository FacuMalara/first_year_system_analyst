"""
Exercise 2.5
The program should:

prompt for two inputs from the console
verify that both inputs are integers
if true, print the sum of both
otherwise, print error
"""

print("Welcome to the console. Two integers will be requested.")

try:
    num_a = input("Insert first integer: ")
    num_b = input("Insert second integer: ")
    if num_a.isnumeric and num_b.isnumeric:
        num_a = int(num_a)
        num_b = int(num_b)
        addition = num_a + num_b
        print(f"This numbers in addition result in: {addition}")
except ValueError as e:
    print(f"Wrong input: {e}")
