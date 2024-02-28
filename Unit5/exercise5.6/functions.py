base_fruits = [['fruit'], ['stock']]  # declaro una lista con dos columas


def ask_string(text_to_ask):
    while True:
        string_variable = input(text_to_ask)
        if string_variable.isalpha():
            break
        else:
            print('you must enter only letters')
    return string_variable.lower()


def ask_int(text_to_ask):
    while True:
        try:
            int_variable = int(input(text_to_ask))
            break
        except Exception as e:
            print('you must enter only numbers')
    return int_variable


def print_base(base_fruits):
    print('-----base fruits------')
    for i in range(len(base_fruits[0])):  # amount of rows
        print(f"{base_fruits[0][i]} \t {base_fruits[1][i]}")


def add_stock(base_fruits):
    print_base(base_fruits)
    new_fruit = ask_string('Enter new fruit: ')
    fruit_stock = ask_int('Enter fruit stock: ')
    base_fruits[0].append(new_fruit)
    base_fruits[1].append(fruit_stock)

    print_base(base_fruits)
    return base_fruits


def consult_stock(base_fruits):
    fruit_to_consult = ask_string(
        'Enter a new fruit to consult stock: ')
    if (fruit_to_consult in base_fruits[0]):
        index = base_fruits[0].index(fruit_to_consult)
        print(f"Stock of {fruit_to_consult} is: {base_fruits[1][index]}")
    else:
        print(f'Fruit {fruit_to_consult} does not belong to stock')


def delete_stock(base_frutas):
    fruit_to_delete = ask_string('Enter a fruit to delete: ')
    if (fruit_to_delete in base_fruits[0]):
        index = base_fruits[0].index(fruit_to_delete)
        base_fruits[0].pop(index)
        base_fruits[1].pop(index)
        print(f"Fruit  {fruit_to_delete} was deleted")
    else:
        print(f'Fruit {fruit_to_delete} does not belong to stock')
    print_base(base_fruits)
    return base_fruits


def descount_stock(base_frutas):
    fruit_to_discount = ask_string(
        'Enter fruit to discount units: ')
    if (fruit_to_discount in base_fruits[0]):
        stock_quantity = ask_int('Amount of stock to reduce: ')
        index = base_fruits[0].index(fruit_to_discount)
        if (base_fruits[1][index] >= stock_quantity):
            base_fruits[1][index] -= stock_quantity
        else:
            print('Stock is not sufficient')
        print(
            f" {stock_quantity} units of the fruit {fruit_to_discount} were discounted")
    else:
        print(f'Fruit {fruit_to_discount} does not belong to stock')
    print_base(base_fruits)
    return base_fruits
