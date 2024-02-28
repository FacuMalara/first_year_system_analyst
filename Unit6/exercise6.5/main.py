from manager import *


def menu():
    obj_manager = ComputerManager()
    while True:
        menu = """

1. Create Computer, indicating type and save in a list. Verifying brand and OS from a list
2. List Computers (presenting them), indicating type.
3. Change OS of a Computer, checking a list of available OS
4. List peripherals
5. Exit """

        option = input(menu)
        match option:
            case '1':
                obj_manager.create_computer()
            case '2':
                obj_manager.list_computers()
            case '3':
                obj_manager.change_SO()
            case '4':
                obj_manager.list_periferics()
            case '5':
                print("Ending process")
                return
            case _:
                print('Incorrect option')


if __name__ == "__main__":
    menu()
