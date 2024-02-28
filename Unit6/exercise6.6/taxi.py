"""
###Exercise 6.6 (Taxi Company)
Simulate a taxi company that has two classes: Car and Driver

The Car class has the attributes (license_plate, model, year, brand, driver_name (object of the Driver class))

The Driver class has the attributes (name, last_name, dni, date_of_birth, residence)"""


class Driver:
    def __init__(self, drivers_name, last_name, identification, birth_date, residence):
        self.drivers_name = drivers_name
        self.last_name = last_name
        self.identification = identification
        self.birth_date = birth_date
        self.residence = residence


class Taxis:
    def __init__(self, license_plate, model, year, brand, drivers_name: Driver):
        self.license_plate = license_plate
        self.model = model
        self.year = year
        self.brand = brand
        self.drivers_name = drivers_name
