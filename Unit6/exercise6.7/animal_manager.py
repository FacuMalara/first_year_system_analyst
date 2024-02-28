"""

Here is a translation of the requirements for the Zoo Management program:

Have 6 functions available in the menu (these functions must be included in a class called ZooManager):

1. Create instances of animals (you can choose between the three sectors) and save them in a list
2. Create an instance of Employees and save them in a list
    Employees can be assigned animals later; the animals must have a caretaker assigned when created in the system
3. Assign an employee to care for an animal
4. Change the caretaker of an animal
5. Print a list of animals (with all their information)
6. Print a list of Employees (with all their information)

The corresponding methods for the menu functions must be created in the corresponding classes

Handle possible errors

Structure the program according to your own criteria
"""

from class_animal import *
from class_employee import *


class ZooManager:
    def __init__(self):
        self.list_of_employees: list[Employee] = []
        self.list_of_animals: list[Animal] = []

    def create_animal(self):
        name = input("Animal´s Name: ")
        type_of_animal = input("Animal´s type: ")
        birth_date = input("Birth date: ")
        option = input("Already has an employee assigned? n/y: ")
        if option == "n":
            assigned_employee = self.create_employee()
        elif option == "y":
            assigned_employee = input("Enter employee ID: ")
            for employee in self.list_of_employees:
                if employee.employee_id == assigned_employee:
                    assigned_employee = employee
                    break
            else:
                print("Employee does not exist")
                return
        else:
            print("Invalid income")
            return
        animal = Animal(name, type_of_animal, birth_date, assigned_employee)
        assigned_employee.list_of_animals_to_take_care.append(animal)
        self.list_of_animals.append(animal)

    def create_employee(self):
        employee_id = input("Employee id: ")
        name = input("Name: ")
        last_name = input("Last name: ")
        employee = Employee(employee_id, name, last_name)
        self.list_of_employees.append(employee)
        return employee

    def assign_animal(self):
        employee_ = self.find_employee(
            "Enter id of an employee you want to assign an animal to take care of: ")
        if not employee_:
            print("Entered id does not belong to an employee in the list")
            return
        animal_ = self.find_animal("Enter animal to take care of: ")
        if not animal_:
            print("Animal is not found in the list")
            return
        employee_.list_of_animals_to_take_care.append(animal_)

    def find_employee(self, text):
        id = input(text)
        for employee in self.list_of_employees:
            if employee.employee_id == id:
                return employee

    def find_animal(self, text):
        name_of_the_animal = input(text)
        for animal in self.list_of_animals:
            if animal.name == name_of_the_animal:
                return animal

    def change_animals_employee(self):
        name_of_the_animal = self.find_animal(
            "Please enter the name of the animal whose caretaker you want to change: ")
        if not name_of_the_animal:
            print("Animal does not exist in the list")
            return
        option = input(
            "To choose an existing caretaker, enter '1'; to create a new one, enter '2'")
        if option == "1":
            employee_id = input("Enter employee id: ")
            original_id = input(
                "Enter the employee's ID who will no longer be taking care of it: ")
            for employee in self.list_of_employees:
                if employee_id == employee.employee_id:
                    name_of_the_animal.assigned_employee = employee
                    employee.list_of_animals_to_take_care.append(
                        name_of_the_animal)
            for employee in self.list_of_employees:
                if original_id == employee.employee_id:
                    employee.list_of_animals_to_take_care.remove(
                        name_of_the_animal)
        elif option == "2":
            original_id = input(
                "Enter the employee's ID who will no longer be taking care of it: ")
            for employee in self.list_of_employees:
                if original_id == employee.employee_id:
                    employee.list_of_animals_to_take_care.remove(
                        name_of_the_animal)
            new_employee = self.create_employee()
            name_of_the_animal.assigned_employee = new_employee
            new_employee.list_of_animals_to_take_care.append(
                name_of_the_animal)
        else:
            print("Incorrect option")

    def print_list_of_animals(self):
        print("----base animals----")
        for animal in self.list_of_animals:
            print(f"Name: {animal.name}\nType: {animal.type_of_animal}\nBirth date: {animal.birth_date}\nAssigned employee: {animal.assigned_employee.name} Last name: {animal.assigned_employee.last_name} Employee id: {animal.assigned_employee.employee_id}")

    def print_list_of_employees(self):
        print("----base employees----")
        for employee in self.list_of_employees:
            print(
                f"Name: {employee.name}\nLast name: {employee.last_name}\nEmployee id: {employee.employee_id}\nList of animals to take care of:")
            for animal in employee.list_of_animals_to_take_care:
                print(f"    - {animal.name}")
