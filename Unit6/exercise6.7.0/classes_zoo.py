'''*   
Simulate a zoo animal management program, which has two classes: Animals and Employees.

The Animals class has the attributes (name, animal_type, date_of_birth, caretaker (Name of employee object))
Create 3 classes that inherit from Animals according to their zoo sector)

1. Animals in cages.
2. Free-range animals.
3. Aquatic animals

The Employees class has the attributes (employee_number, first_name, last_name, list_of_animals_to_care_for (animal class))
An employee can care for animals from different sectors.
'''


class Animal:  # Clase padre
    def __init__(self, name, type_of_animal, birth_date, assigned_employee):
        self.name = name
        self.type_of_animal = type_of_animal
        self.birth_date = birth_date
        self.assigned_employee: Employee = assigned_employee

    def present_animal(self):
        print(f'→ NAME: {self.name} - TYPE: {self.type_of_animal} - BIRTH DATE: {self.birth_date} - EMPLOYEE: {self.assigned_employee.name} {self.assigned_employee.last_name}, EMPLOYEE ID {self.assigned_employee.employee_id}')  # ACA


class CagedAnimal(Animal):
    pass


class LooseAnimal(Animal):
    pass


class AquaticAnimal(Animal):
    pass


class Employee:  # Clase padre
    def __init__(self, employee_id, name, last_name):
        self.employee_id = employee_id
        self.name = name
        self.last_name = last_name
        self.list_of_animals_to_take_care: list[Animal] = []

    def present_employee(self):
        print(
            f'→ EMPLOYEE ID: {self.employee_id} - NAME: {self.name} - LAST NAME: {self.last_name}')
        print('ANIMALS TO TAKE CARE OF: ')
        for animal in self.list_of_animals_to_take_care:
            print(f'     Animal: {animal.name}')  # ACA
