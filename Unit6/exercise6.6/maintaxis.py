from taxismanager import *


def main():

    obj_manager = TaxisManager()

    while True:
        menu = input("""

1. Create instances of drivers and save them in a list of drivers
2. Create instances of cars (checking that there are drivers for that car) and save them in a list of cars
3. Modify the driver of a car
4. Modify the residence of the driver by indicating their name
5. Print list of drivers (with all their information)
6. Print list of cars (with all their information)
7. Exit
                     
Insert option: 
""")

        match menu:
            case '1':
                obj_manager.create_drivers()
            case '2':
                obj_manager.create_taxis()
            case '3':
                obj_manager.modify_driver()
            case '4':
                obj_manager.modify_residence()
            case '5':
                obj_manager.print_drivers_list()
            case "6":
                obj_manager.print_car_list()
            case "7":
                print("Quiting")
                return
            case _:
                print('Incorrect income')


if __name__ == "__main__":
    main()
