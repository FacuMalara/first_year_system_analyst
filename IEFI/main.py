from classes import *
from manager import *


def menu():
    obj_manager = EventManager()

    while True:
        menu = """-- Program Schedule --
    1. Create event
    2. List events
    3. Out
Insert option: """
        option = input(menu)
        if (option == "1"):
            obj_manager.create_event()
        elif (option == "2"):
            obj_manager.read_event_list()
        elif (option == "3"):
            exit()
        else:
            print('Incorrect option')


if __name__ == "__main__":
    menu()
