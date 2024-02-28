"""
Exercise 7.7
Create a program with four options:

Create a blank file, with the name the user desires
Write data to the file without overwriting existing content
Delete the data from the file
Read the file line by line
"""

from class_read_write import *


def main():
    obj_reader = ReadWriter()
    while True:
        menu = input("""
1. Create a blank file, with the name the user desires
2. Write data to the file without overwriting existing content
3. Delete the data from the file
4. Read the file line by line
5. Exit
                     
Insert option:
""")
        match menu:
            case "1":
                obj_reader.create_blanc_file()
            case "2":
                obj_reader.write_data()
            case "3":
                obj_reader.truncate_file()
            case "4":
                obj_reader.read_line_to_line()
            case "5":
                print("Ending process")
                obj_reader.close_file()
                return
            case _:
                print("Invalid income")


if __name__ == "__main__":
    main()
