"""

Exercise 3.16
The program should:

display the echo of everything the user enters
until the user writes "exit"
that will end.
if the user writes "hello" or "bye" the echo should not be done
"""

while True:
    smth = input("Enter something: ")
    print(smth)
    if smth == "hi" or smth == "bye":
        continue
    elif smth == "out":
        break
    else:
        print(smth)
