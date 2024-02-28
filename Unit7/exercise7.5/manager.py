"""

Exercise 7.5 (MISSING)
Create a class to read files (FileReader).

Create functions to:

Read the file and print its entire contents
Find the number of commas in the file.
Count the number of 3-letter words and store them in a list
Specify a word to remove and print the content without this word
"""

import os


class FileReader:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__))

    def open_file(self, name_of_file):
        try:
            self.file = open(f"{self.path}//{name_of_file}", "r")
        except:
            print("File does not exist")

    def close_file(self):
        try:
            self.file.close()
        except:
            print("File does not exist")

    def read_complete_file(self):
        self.open_file("file.txt")
        try:
            print(self.file.read())
            self.file.seek(0)
        except:
            print("File does not exist")

    def read_save_file(self):
        try:
            text = self.file.read()
            self.file.seek(0)
            return text
        except:
            print("File was not found")
            return ""

    def find_amount_comas(self):
        self.open_file("file.txt")
        text = self.read_save_file()
        count = 0
        for char in text:
            if char == ",":
                count += 1
        print(f"There were found {count} comas")

    def words_of_three(self):
        self.open_file("file.txt")
        text = self.read_save_file().replace("\n", " ").replace(
            ".", " ").replace(",", " ").split(" ")
        count = 0
        for word in text:
            if len(word) == 3:
                print(word)
                count += 1
        print(f"There were found {count} words of three")

    def remove_word(self):
        self.open_file("archivo.txt")
        text = self.read_save_file().replace("\n", " ").replace(
            ".", " ").replace(",", " ").split(" ")
        for word in text:
            if word == "":
                text.remove(word)
        text_list = text
        word_to_remove = input("Entera a word to remove: ")
        if word_to_remove in text_list:
            for word in text_list:
                if word == word_to_remove:
                    text_list.remove(word)
            print(text_list)
        else:
            print("The specified word does not exist")
