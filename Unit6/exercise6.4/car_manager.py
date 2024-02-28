'''
Create a class CarManager that has the following functions for a menu:

Create a car, indicating the type of car and save it in a list.
List cars (presenting them), indicating the type of vehicle.
Change the speed of a vehicle.
Calculate the travel time of a vehicle over a certain distance in kilometers passed as a parameter (time = Km / Speed).'''

from car import *


class CarManager:
    def __init__(self):
        self.car_list: list[Car] = []

    def create_car(self):
        license_plate = input("Give me a license plate: ")
        origin = input("Give me an origin: ")
        year = input("Give me an year: ")
        brand = input("Give me a brand: ")
        speed = self.ask_speed("Give me a max speed(km/h): ")
        type_ = input("Give me a valid type: ").lower()
        if type_ == "particular":
            seats = input("How many seats do you want? ")
            object_car = Particular(
                license_plate, brand, year, origin, speed, seats)
        elif type_ == "pickup":
            gas_type = input("Diesel/Infinia: ")
            object_car = PickUp(license_plate, brand, year,
                                origin, speed, gas_type)
        elif type_ == "sportscar":
            turbo = input("Turbo? Y/N: ")
            object_car = SportsCar(
                license_plate, brand, year, origin, speed, turbo)
        self.car_list.append(object_car)

    def calculate(self):
        id_car = input("Insert license_plate: ")
        km = self.ask_speed("Distance(km): ")
        for car in self.car_list:
            if car.license_plate == id_car:
                speed = car.get_speed()
            else:
                print("Incorrect income")
        time = km / speed
        print(f"Approximate time {time} hours")

    def ask_speed(self, text):
        while True:
            try:
                speed = input(text)
                if speed.isnumeric():
                    speed = int(speed)
                    return speed
                else:
                    print("Incorrect")
            except ValueError as e:
                print(f"Invalid income {e}")

    def change_speed(self):
        license_ = input("Insert license plate: ")
        for car in self.car_list:
            if car.license_plate == license_:
                option = input("Speed up/Reverse/set speed manually: ").lower()
                if option == "speed up":
                    accelerator = self.ask_speed("Insert int modifier: ")
                    car.speed_up(accelerator)
                elif option == "reverse":
                    accelerator = self.ask_speed("Insert int modifier: ")
                    car.reverse(accelerator)
                elif option == "set speed manually":
                    car.set_speed()
                else:
                    print("Invalid income")
            else:
                print("Wrong plate")

    def list_cars(self):
        for car in self.car_list:
            car.types()
            car.present()
