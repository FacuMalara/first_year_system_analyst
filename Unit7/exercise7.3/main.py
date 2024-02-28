"""
Exercise 7.3
Create a function to read a .txt file.

Create functions to:

Count the number of letters in the file (letters, not spaces or periods).
Count the number of words in the file."""

import os


def get_path():
    return os.path.abspath(os.path.dirname(__file__))


def read_file(file):
    try:
        file = open(f"{get_path()}//{file}", "r")
        text = file.read()
        file.close()
        return text
    except:
        print("File does not exist")
        return ""


def count_words():
    text = read_file("file.txt")
    clean_text = text.replace(".", "").replace(
        ",", "").replace(";", "").replace("\n", "")
    text_list = clean_text.split(" ")
    print(text_list)
    count = 0
    for word in text_list:
        count += 1
    print(f"There are {count} words in this text")


def count_letters():
    text = read_file("file.txt")
    clean_text = text.replace(".", "").replace(
        ",", "").replace(";", "").replace("\n", "").replace(" ", "")
    letters = len(clean_text)
    print(f"There are {letters} in this text")


count_words()
count_letters()
