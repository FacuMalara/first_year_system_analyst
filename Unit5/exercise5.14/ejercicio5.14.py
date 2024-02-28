"""
Exercise 5.14
Create a function that should: (use a dictionary)

Create an empty dictionary and fill it with information about
a person (for example name, age, gender, phone number, email, etc.)
Ask the user for the key (data to add) and the value
Each time a new data is added, the content of the dictionary should be printed.
"""

list_of_people = dict()
while True:
    key = input("Insert key: ")
    value = input("Enter corresponding value: ")
    if key not in list_of_people:
        list_of_people.update({key: value})
        print("-----list of people-----")
        for i, j in list_of_people.items():
            print(f"{i} {j}")
    else:
        print("Value already exists")
    decision = input("Do you want to make another income? y/n: ")
    if decision.lower() == "n":
        break
