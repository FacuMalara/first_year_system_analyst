"""Ejercicio 7.2
Create a function to read a .txt file. Ask the user for a word 
and find the number of times that word appears in the file."""

import os


def get_path():
    return os.path.abspath(os.path.dirname(__file__))


def read_full_file(file):
    try:
        file = open(f"{get_path()}//file.txt", 'r')
        file_text = file.read()
        file.close()
        return file_text

    except:
        print("File was not found")
        return ''


def contar_palabras():
    file_text = read_full_file('file.txt')
    clean_text = file_text.replace(".", "").replace("\n", "")
    new_text = clean_text.split(" ")
    print(new_text)
    word_to_search = input("Enter word to search: ")
    count = 0
    for word in new_text:
        if word == word_to_search:
            count += 1
    print(f"There are {count} {word_to_search} in this text")


contar_palabras()
