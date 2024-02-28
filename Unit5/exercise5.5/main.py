from functions import *


def main():
    while True:
        ask()
        a = input("Want to make another calculus? y/n: ")
        if a.lower() == "n":
            print("Ending process")
            return


if __name__ == "__main__":
    main()
