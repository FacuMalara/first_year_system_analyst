"""

Exercise 5.13
Create a function that should: (use a dictionary)

Save the prices of the fruits from the table in a dictionary.
Ask the user for a fruit and a number of kilos, and display on the screen
the price of that number of kilos of fruit.
If the fruit is not in the dictionary, it should display an ERROR message.
Fruit Price
banana 50
apple 80
pear 100
orange 30

"""
try:
    fruits = {"banana": 50, "apple": 80, "pear": 100, "orange": 30}
    chosen_fruit = input("Choose a fruit: ")
    if chosen_fruit in fruits.keys():
        kilos = int(input("Enter amount of kilos: "))
        for i, j in fruits.items():
            if i == chosen_fruit:
                total = j * kilos
        print(f"Amount to pay: {total}")
except:
    print("Invalid income")
