def ask_number(text_to_ask):
    while True:
        number = input(text_to_ask)
        if number.isnumeric():
            new_number = int(number)
            return new_number
        else:
            print("Enter positive numbers")


# funcion opcion 1
def add_fruits(list_of_fruits):
    fruit = input("Enter fruit to add: ")
    if fruit not in list_of_fruits[0]:
        list_of_fruits[0].append(fruit)
        cant_fruta = ask_number("Enter number of units: ")
        list_of_fruits[1].append(cant_fruta)
        print("Correctly registered")
    elif fruit in list_of_fruits:
        print("Fruit already exists on the list")
    else:
        print("Invalid character entered")
    return list_of_fruits


def consult_stock(list_of_fruits):
    print("---BASE FRUITS---")
    for i in range(len(list_of_fruits[0])):
        print(f"{list_of_fruits[0][i]}--{list_of_fruits[1][i]}")


def delete_fruit(list_of_fruits):
    fruit_to_delete = input("Ingrese fruta a eliminar: ")
    if fruit_to_delete in list_of_fruits[0]:
        index = list_of_fruits[0].index(fruit_to_delete)
        list_of_fruits[0].pop(index)
        list_of_fruits[1].pop(index)
        print("Removed")
    else:
        print("Inserted data does not belong to list or is invalid")
    return list_of_fruits


def discount_units(list_of_fruits):
    fruit_to_discount = input("Enter fruit you wish to discount units: ")
    if fruit_to_discount in list_of_fruits[0]:
        amount_to_discount = ask_number("Enter number of units to discount: ")
        index = list_of_fruits[0].index(fruit_to_discount)
        if amount_to_discount >= 0 and list_of_fruits[1][index] >= amount_to_discount:
            new_amount = list_of_fruits[1][index] - amount_to_discount
            list_of_fruits[1].pop(index)
            list_of_fruits[1].insert(index, new_amount)
            print(f"New amount is {new_amount}")
        elif amount_to_discount > 0 and list_of_fruits[1][index] < amount_to_discount:
            new_amount = 0
            print("Warning")
            print(
                "Bigger number than the current existence was entered, the amount cannot be less than cero")
            print(f"New amount {new_amount}")
    else:
        print("Entered fruit does not belong to the list")
    return list_of_fruits


def add_stock(list_of_fruits):
    fruit_to_add = input("Enter fruit to add units: ")
    if fruit_to_add in list_of_fruits[0]:
        amount_to_add = ask_number("Enter number of units to add: ")
        index = list_of_fruits[0].index(fruit_to_add)
        new_amount = list_of_fruits[1][index] + amount_to_add
        list_of_fruits[1].pop(index)
        list_of_fruits[1].insert(index, new_amount)
        print(f"New amount is {new_amount}")
    else:
        print("Specified fruit does not belong to list")
    return list_of_fruits
