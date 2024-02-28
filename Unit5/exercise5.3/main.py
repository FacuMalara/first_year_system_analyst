from functions import *


def main():
    while True:
        try:
            word = ask_word("Enter word: ")
            new_word = new_word_(word)
            if new_word.isalpha():
                palindrome = reversed_word(new_word)
                print(new_word, palindrome)
                print(new_word == palindrome)
                break
            else:
                print("Entered chain conteins character that is not alphabetic")
        except ValueError as e:
            print(f"Invalid datum {e}")


if __name__ == "__main__":
    main()
