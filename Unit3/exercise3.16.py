"""
Exercise 3.16
The program should:

display the echo of everything the user enters
until the user writes "exit"
that will end.
if the user writes "hello" or "bye" the echo should not be done
"""

while True:
    eco = input("Enter something: ")
    if eco == "hi" or eco == "bye":
        print(eco)
    elif eco == "out":
        break
    else:
        print(eco)
        print(eco)
