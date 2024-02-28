from stock_frutas import *


def ask_text(ask_for_text):
    while True:
        new_text = input(ask_for_text).lower()
        if new_text.isalpha():
            return new_text
        else:
            print("Enter only letters")


def ask_number(text_for_number):
    while True:
        try:
            new_number = (input(text_for_number))
            if new_number.isnumeric():
                new_number = int(new_number)
                return new_number
        except ValueError as e:
            print(f"Enter numbers {e}")


def add_fruit(test):
    try:
        fruit_to_add = ask_text("Enter fruit to incorporate: ").lower()
        amount_to_add = ask_number("Enter quantity: ")
        test.append(StockFrutas(fruit_to_add, int(amount_to_add)))
        print_list(test)
        return test
    except ValueError as e:
        print(f"Invalid {e}")


def consult_stock(test):
    fruit_to_consult = ask_text("Enter fruit to consult: ")
    for i in test:
        if fruit_to_consult == i.name:
            print(f'Stock of {i.name} is about {i.value}')


def delete_fruit(test):
    fruit_to_delete = ask_text("Enter fruit to delete: ")
    if fruit_to_delete in test[0]:
        test.pop(StockFrutas(fruit_to_delete.name, fruit_to_delete.value))
    else:
        print("Entered fruit does not belong to stock")
    print(test)
    return test


def discount_units(test):
    fruit_to_discount = ask_text(
        "Enter fruit to discount units: ").lower()
    amount_units_discount = ask_number("Enter amount of units to discount: ")
    if fruit_to_discount in test[0]:
        test(StockFrutas(fruit_to_discount.name,
             fruit_to_discount.value-amount_units_discount))
    else:
        print("Fruit does not belong to stock")
    return test


def print_list(test):
    # for i in list[0]:
    # print(list[0, i])
    print(test)
    return test
