"""
Exercise 7.6
Create a function that asks the user for words and writes them to a text file, each word on a new line.
"""

import os


def get_path():
    return os.path.abspath(os.path.dirname(__file__))


def write_file():
    file = open(f"{get_path()}//archivo.txt", "+a")
    print("If you wish to finish write finish")
    word = input("Enter words to add: ")
    while word != "End process":
        file.write(word+" ")
        word = input("Enter a word to add: ")
    file.close()


write_file()
