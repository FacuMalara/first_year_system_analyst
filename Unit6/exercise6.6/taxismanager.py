"""
###Exercise 6.6 (Taxi Company)
Simulate a taxi company that has two classes: Cars and Drivers

The Car class has the attributes (license_plate, model, year, brand, driver_name (object of the Drivers class))

The Driver class has the attributes (name, last_name, dni, date_of_birth, residence)

Have 6 functions available in the menu (these functions must be included in a class called TaxiManager):

Create instances of drivers and save them in a list of drivers
Create instances of Cars (checking that there are drivers for that car) and save them in a list of cars
Modify the driver of a car
Modify the residence of the driver indicating his name
Print list of drivers (with all their information)
Print list of cars (with all their information)
The methods corresponding to the menu functions must be created in the corresponding classes

"""


from taxi import *


class TaxisManager:
    def __init__(self):
        self.list_taxis: list[Taxis] = []
        self.list_drivers: list[Driver] = []

    def create_drivers(self):
        drivers_name = input("Insert drivers name: ")
        last_name = input("Insert drivers last name: ")
        identification = input("Insert drivers identification: ")
        brith_date = input("Insert drivers birth date: ")
        residence = input("Insert drivers residence: ")
        driver = Driver(drivers_name, last_name,
                        identification, brith_date, residence)
        self.list_drivers.append(driver)

    def create_taxis(self):
        license_plate = input("Insert license plate: ")
        model = input("Insert model: ")
        year = input("Insert realese date: ")
        brand = input("Insert brand: ")
        drivers_name = self.choice("Have driver/create new: ")
        taxi = Taxis(license_plate, model, year, brand, drivers_name)
        self.list_taxis.append(taxi)
        print("New taxi created with driver associated")

    def choice(self, text):
        while True:
            option = input(text).lower()
            match option:
                case "have driver":
                    drivers_id = input("Insert drivers identification: ")
                    for driver in self.list_drivers:
                        if drivers_id == driver.identification:
                            drivers_name = driver
                            print("Correct income")
                            return drivers_name
                        else:
                            print("Drivers id is not found in the system")
                case "create new":
                    drivers_name: Driver = self.create_drivers()
                    return drivers_name
                case _:
                    print("wrong option")

    def modify_driver(self):
        taxi_plate = input("Give me a license_plate: ")
        for taxi in self.list_taxis:
            if taxi_plate == taxi.license_plate:
                taxi.drivers_name: Driver = self.choice(
                    "Have driver/create new: ")
            else:
                print("Wrong plate")

    def modify_residence(self):
        drivers_id = input("Insert drivers id: ")
        for driver in self.list_drivers:
            if drivers_id == driver.identification:
                driver.residence = input("Insert new residence: ")

    def print_drivers_list(self):
        print("---base drivers---")
        count = 1
        for driver in self.list_drivers:
            print(f"Driver {count}:\nName:{driver.drivers_name}\nLast name: {driver.last_name}\nId: {driver.identification}\nBirth Date: {driver.birth_date}\nResidence: {driver.residence}")
            count += 1

    def print_car_list(self):
        print("----base taxis----")
        count = 1
        for taxi in self.list_taxis:
            for driver in self.list_drivers:
                if driver == taxi.drivers_name:
                    print(
                        f"Taxi {count}:\nLicense Plate:{taxi.license_plate}\nModel: {taxi.model}\nYear: {taxi.year}\nBrand: {taxi.brand}\nDriver associated:{driver.drivers_name}")
                    count += 1

    def print_(self):
        for taxi in self.list_taxis:

            print(f"{taxi.drivers_name.drivers_name}")
    # forma mas facil de hacer la funcion de arriba

# al llamar al objeto gestor crea 2 listas vacias, puedo acceder a cada una de acuerdo a los llamados que haga
