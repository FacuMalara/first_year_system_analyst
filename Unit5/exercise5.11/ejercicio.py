"""

##Exercise 5.11
Create a function that should: (use a dictionary)

Contain a dictionary with different currencies of countries, where:
The key is the name of the currency and the value is the symbol.
Ask the user which type of currency they want and display the symbol
if it exists in the dictionary, otherwise indicate that it does not exist."""

currencies = {
    "Peso": "$",
    "Dolar": "USD",
    "Euro":  "€"
}


def get_simbol():
    currencies_ = input('Enter curriencie to search: ').capitalize()
    print(currencies.get(currencies_, 'Currencie does not exist in the dictionary'))


get_simbol()
