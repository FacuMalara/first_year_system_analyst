from car_manager import *


def main():
    obj_manager = CarManager()
    while True:
        menu = """
1. Create a car, indicating the type of car and save it in a list.
2. List cars (presenting them), indicating the type of vehicle.
3. Change the speed of a vehicle.
4. Calculate the travel time of a vehicle over a certain distance in kilometers passed as a parameter (time = Km / Speed).
5. Exit

Enter option: 
"""
        option = input(menu)
        match option:
            case '1':
                obj_manager.create_car()
            case '2':
                obj_manager.list_cars()
            case '3':
                obj_manager.change_speed()
            case '4':
                obj_manager.calculate()
            case '5':
                print("Ending process")
                return
            case _:
                print('Incorrect option')


if __name__ == "__main__":
    main()
