from manager import *


def main():
    obj_reader = FileReader()

    while True:
        menu = input("""

1. Read the file and print its entire contents.
2. Find the number of commas in the file.
3. Count the number of 3-letter words and save them in a list.
4. Specify a word to remove and print the content without this word.
5. Exit
                     
Insert option: 
""")
        match menu:
            case "1":
                obj_reader.read_complete_file()
            case "2":
                obj_reader.find_amount_comas()
            case "3":
                obj_reader.words_of_three()
            case "4":
                obj_reader.remove_word()
            case "5":
                print("Ending process")
                obj_reader.close_file()
                return
            case _:
                print("Invalid access")


if __name__ == "__main__":
    main()
