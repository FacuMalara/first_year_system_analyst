"""
Exercise 3.14

The program should:

ask the user for a data
only if the user writes the keyword "python", print "Correct" on the screen, otherwise it should continue asking for the data
no errors should appear."""

datum = ""
flag = True
while flag:
    datum = input("insert datum: ")
    if datum.lower() == ("python"):
        print("Correct")
        flag = False
