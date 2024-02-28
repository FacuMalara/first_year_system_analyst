"""
Exercise 3.17
The program should:

Ask the user for a phrase and a letter
display on the screen the number of times 
the letter appears in the phrase.
"""

frase = input("Enter a frase: ")
word_a = input("Enter a word: ")
count = 0

for word in frase:
    if word == word_a:
        count += 1
        print(count)
