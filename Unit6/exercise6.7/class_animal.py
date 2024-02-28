"""
The Class Animals has the attributes (name, animal_type, date_of_birth, caretaker (Name of employee object))

Create 3 classes that inherit from animal according to their zoo sector)
Animals in cages.
Free animals.
Water animals
The Class Employees has the attributes (file_number, name, last_name, list_of_animals_to_take_care
(animal class))

"""


class Animal:
    def __init__(self, name, type_of_animal, birth_date, assigned_employee):
        self.name = name
        self.type_of_animal = type_of_animal
        self.birth_date = birth_date
        self.assigned_employee = assigned_employee

    def change_employee(self, new_employee):
        self.assigned_employee = new_employee


class CageAnimal(Animal):
    pass


class LooseAnimal(Animal):
    pass


class AquaticAnimal(Animal):
    pass
