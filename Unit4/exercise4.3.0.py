"""

Exercise 4.3 (Words)
The program should:

Have 3 functions:
Letter counter (letter, word): It should count the number of letters in a word or phrase (Both parameters)

Word comparator (word1 vs word2): It should compare which word has more letters. IMPORTANT: they must be words and not phrases (verify)

Vowel remover (word to remove vowels from): It should receive a word or phrase and remove all vowels

Have a menu where it should ask the user which operation to perform

Ask for the parameters and return the result to the user

Handle possible errors"""


def countletters(word):
    counter = 0

    word = word.replace(" ", "")
    for letter in word:
        counter += 1
    print(f'It has {counter} letters.')


def comparator(word1, word2):
    counter1 = 0
    counter2 = 0

    for i in word1:
        counter1 += 1
    for i in word2:
        counter2 += 1

    if counter1 > counter2:
        print('First word is the bigger.')
    else:
        print('Second word is bigger.')


def get_vocals(word):
    no_vocal_word = ""

    for letter in word:
        if letter in 'aeiou':
            pass
        else:
            no_vocal_word += letter
    print(f'Word without vocals is: {no_vocal_word}')


def verify_word():
    while True:
        word1 = input('Enter first word: ')
        if word1.find(' ') >= 0:
            print('Enter word, not a phrase')
            continue

        word2 = input('Enter second word:')
        if word2.find(' ') >= 0:
            print('Enter word, not a phrase')

        else:
            return word1, word2

# Main


# Init
option = 0
word = None
while True:
    try:
        print('''
          
Choose one of the options:
1 - Count letters.
2 - Compare words.
3 - Remove vowels.
4 - Exit.
          ''')

        option = int(input('Enter an option: '))

        match option:

            case 1:
                word = input('Enter a word: ')
                countletters(word)

            case 2:
                word1, word2 = verify_word()
                comparator(word1, word2)

            case 3:
                word = input('Enter a word: ')
                get_vocals(word)

            case 4:
                print('Ending process')
                break

            case _:
                print('Incorrect option.')
    except:
        print('Enter valid option')
