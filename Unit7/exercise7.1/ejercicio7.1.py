"""
Exercise 7.1
Create a function to read a .txt file until finding a period.
"""

import os


def get_path():
    return os.path.abspath(os.path.dirname(__file__))


try:
    file = open(f"{get_path()}//""file.txt", 'r')
    char = file.readline(1)
    while char != "":
        if char == ".":
            print(char)
        char = file.readline(1)
    file.close()
except:
    print("File does not exist")
