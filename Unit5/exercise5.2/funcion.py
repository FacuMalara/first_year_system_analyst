"""
Exercise 5.2
Create a function that should: (use lists)

Ask the user for the number of people
Ask the user one by one for the age of the people
After loading the ages, it should print the oldest age on the screen
No errors should appear and all possible errors must be taken into
 account"""


def ask_int(text_to_ask):
    while True:
        try:
            int_variable = int(input(text_to_ask))
            break
        except Exception as e:
            print('You must enter numeric value!')
    return int_variable


def main():
    list = []
    amount_people = ask_int('Enter amount of people: ')
    for i in range(0, amount_people):
        age = ask_int(f'Enter persons age {i+1}: ')
        list.append(age)
    list.sort()
    print(f'Bigger age in the list is: {list[-1]}')


if __name__ == "__main__":
    main()
