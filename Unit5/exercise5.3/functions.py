def ask_word(text):
    """function to ask a word"""
    word = input(text)
    return word


def new_word_(word):
    new_word = ""
    for char in word:
        if char != " ":
            new_word += char
    return new_word


def reversed_word(new_word):
    palindrome = ""
    for char in new_word:
        palindrome = char + palindrome
    return palindrome
