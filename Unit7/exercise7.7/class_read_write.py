"""

Exercise 7.7
Create a program with four options:

Create a blank file with the name chosen by the user.
Write data to the file without overwriting existing data.
Delete the data from the file.
Read the file line by line.
"""

import os


class ReadWriter:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__))

    def file_name(self):
        file_name = input("Enter file name: ")
        if file_name in self.file:
            self.open_file(file_name)
        else:
            print("File not found")
            return ""

    def open_file(self, file_name):
        try:
            self.file = open(f"{self.path}//{file_name}", "+a")
        except:
            print("File does not exist")

    def close_file(self):
        try:
            self.file.close()
        except:
            print("File does not exist")

    def create_blanc_file(self):
        file_name = input("Enter new file´s name: ")
        self.open_file(file_name)

    def write_data(self):
        self.file_name()
        if self.file:
            datum = input("Enter datum: ")
            data = []
            while datum != "Finish process":
                data.append(datum)
                datum = input("Enter datum ")
            option = input("Space or line break (1/2): ")
            for datum in data:
                if option != "1" and option != "2":
                    print("Incorrect option")
                    break
                else:
                    while True:
                        if option == "1":
                            self.file.write(datum + " ")
                            break
                        elif option == "2":
                            self.file.write(datum + "\n")
                            break
            self.file.seek(0)
            print(self.file.read())
            self.file.seek(0)
        else:
            print("Incorrect")

    def truncate_file(self):
        self.file_name()
        self.file.truncate(0)
        self.file.seek(0)
        print(self.file.read())
        self.file.seek(0)

    def read_line_to_line(self):
        try:
            file_name = input("Enter file´s name: ")
            self.file = open(f"{self.path}//{file_name}", "r")
            line = self.file.readline()
            while line != "":
                print(line, end="")
                line = self.file.readline()
        except:
            print("Wrong income")
