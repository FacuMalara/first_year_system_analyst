"""
Exercise 3.18
The program should:

Ask the user for a positive integer and display
on the screen the countdown from that number to
zero separated by commas.
Example: num = 8.

8,7,6,5,4,3,2,1,
"""

try:
    num = int(input("Enter a possitive integer: "))
    if num > 0:
        for i in range(num, 0, -1):
            print(i)
    else:
        print("You entered a negative number")
except ValueError as e:
    print(f"Error {e}")
