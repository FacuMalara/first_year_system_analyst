"""

##Exercise 5.12
Create a function that should: (use a dictionary)

Ask the user for their name, age, address, and phone number, and store it
in a dictionary.
Display the message: "name" is "age" years old, lives
at "address", and their phone number is "phone" with all the data from
the dictionary"""


def get_info():
    people_dictionary = {}
    name = input('Enter name: ')
    age = input('Enter age: ')
    address = input('Enter address: ')
    telephone = input('Enter telephone number: ')
    people_dictionary.update(
        {'name': name, 'age': age, 'direction': address, 'telephone': telephone})
    print(f"- name: {people_dictionary.get('name')}\
            - age: {people_dictionary.get('age')}\
            - direction: {people_dictionary.get('direction')}\
            - telephone: {people_dictionary.get('telephone')}")


get_info()
