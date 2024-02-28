"""
Create a class Car:

The constructor must include the attributes (license plate, brand, year, origin)
Create methods for this class:

1. Introduce (license plate, brand, year, origin)
2. Indicate types of vehicles (Inherited classes)
3. Methods that will later modify the child classes. Accelerate, Reverse, get_speed, set_speed
    Create 3 classes that inherit from the parent class Vehicle, with a particular attribute for each one

    1. Personal
    2. Pickup
    3. Sports"""


class Car:
    def __init__(self, license_plate, brand, year, origin, speed):
        self.license_plate = license_plate
        self.brand = brand
        self.year = year
        self.origin = origin
        self.speed = speed

    def present(self):
        print(
            f"This is a car from the brand {self.brand}, year {self.year}, has this license plate {self.license_plate}, manufactured on {self.origin} and max speed {self.speed}km/h")

    def types(self):
        print(f"This is a car of type: {type(self).__name__}")

    def speed_up(self, accelerator):
        self.speed = self.speed * accelerator
        print(f"New speed: {self.speed}")

    def reverse(self, accelerator):
        self.speed = self.speed / accelerator
        print(f"New speed: {self.speed}")

    def get_speed(self):
        while True:
            try:
                speed = input("At which speed(int): ")
                if speed.isnumeric():
                    speed = int(speed)
                    return speed
                else:
                    print("Incorrect")
            except ValueError as e:
                print(f"Invalid income {e}")

    def set_speed(self):
        while True:
            try:
                speed = input("Set the new speed(int): ")
                if speed.isnumeric():
                    speed = int(speed)
                    self.speed = speed
                    print(f"New speed is set: {self.speed}")
                    break
                else:
                    print("Incorrect")
            except ValueError as e:
                print(f"Invalid income {e}")


class Particular(Car):
    def __init__(self, license_plate, brand, year, origin, speed, seats):
        super().__init__(license_plate, brand, year, origin, speed)
        self.seats = seats


class PickUp(Car):
    def __init__(self, license_plate, brand, year, origin, speed, gas_type):
        super().__init__(license_plate, brand, year, origin, speed)
        self.gas_type = gas_type


class SportsCar(Car):
    def __init__(self, license_plate, brand, year, origin, speed, turbo):
        super().__init__(license_plate, brand, year, origin, speed)
        self.turbo = turbo
