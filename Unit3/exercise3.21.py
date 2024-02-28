"""
Exercise 3.21
The program should:

Ask the user for a word
Verify that it is a word and not a number
Display the letters one by one on the screen
Not produce errors
"""

word = ""

while word.lower() != "out":
    word = input("Enter word: ")
    if word.isalpha():
        for char in word:
            print(char)
    elif word.lower() == "out":
        break
    else:
        print("Enter only words")
