from class_animal import *


class Employee:
    def __init__(self, employee_id, name, last_name):
        self.employee_id = employee_id
        self.name = name
        self.last_name = last_name
        self.list_of_animals_to_take_care: list[Animal] = []

    def add_animal(self, animal_to_add):
        self.list_of_animals_to_take_care.append(animal_to_add)
