"""
###Exercise 4.3 (Words)
The program should:

Have 3 functions:
Letter counter (letter, word): It should count the number of letters in a word or phrase (Both parameters)

Word comparator (word1 vs word2): It should compare which word has more letters. IMPORTANT: they must be words and not phrases (verify)

Vowel remover (word to remove vowels from): It should receive a word or phrase and remove all vowels

Have a menu where it should ask the user which operation to perform

Ask for the parameters and return the result to the user

Handle possible errors

"""


def count_(word_frase):
    word_frase = word_frase.replace(" ", "")
    try:
        if word_frase.isalpha():
            count = 0
            for count in range(len(word_frase)):
                count += 1
            print(f"There is {count} words in the element")
        else:
            print("You entered wrong info")
    except ValueError as e:
        print(f"ERROR {e}")


def comparator(word1, word2):
    try:
        while True:
            if word1.isspace() or word2.isspace():
                print("You entered phrases")
            else:
                if len(word1) == len(word2):
                    print("Equal length")
                elif len(word1) > len(word2):
                    print("First word is longer")
                else:
                    print("Second word is longer")
                break
    except ValueError as e:
        print(f"ERROR {e}")


def remover(word_frase):
    try:
        word_frase = word_frase.replace("aeiou", "")
        print(f"New phrase or word {word_frase}")
    except ValueError as e:
        print(f"ERROR {e}")


def main():
    while True:
        menu = """
                
Welcome to the menu
1. Count word or phrase
2. Compare two words
3. Remove vowels from word or phrase
4. Exit
                """
        option = input(menu)
        if option == "1":
            text1 = input("Enter word or phrase: ")
        elif option == "2":
            text2 = input("Enter word: ")
            text3 = input("Enter another word: ")
        elif option == "3":
            text4 = input("Enter word or phrase: ")

        match option:
            case "1":
                count_(text1)
            case "2":
                comparator(text2, text3)
            case "3":
                remover(text4)
            case "4":
                break
            case _:
                print("Wrong income")


main()
