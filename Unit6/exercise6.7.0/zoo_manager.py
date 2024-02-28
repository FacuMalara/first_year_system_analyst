'''*   Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorZoologico)**:
    1. Crear instancias de animales (se puede elegir entre los tres sectores)  y guardarlos en una lista
    2. Crear instancia de Empleados y guardarlos en una lista
        * Los empleados se les pueden asignar animales luego, los animales al crearlos en el sistema tienen q contar siosi con un encargado
    3. Asignar a un empleado un animal a cuidar
    4. Cambiar de encargado un animal
    5. imprmiir lista de animales (con toda su informacions)
    6. imprimir lista de Empleados (con toda su informacions)

*   Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio'''

from classes_zoo import *


class ZooManager:
    def __init__(self):
        self.list_of_animals: list[Animal] = []
        self.list_of_employees: list[Employee] = []

    def create_animal(self):
        if (len(self.list_of_employees) == 0):
            print('No employees available: \n')
        else:
            name = input('Enter animal´s name: \n')
            type_of_animal = input('Enter animal´s type: \n')
            birth_date = input(
                'Enter animal´s birth date: \n')

            for employee in self.list_of_employees:
                employee.present_employee()
            employee_id = input(
                'Enter the employee ID you want to assign to this animal.: \n')

            for employee in self.list_of_employees:
                if (employee_id == employee.employee_id):
                    new_animal = Animal(
                        name, type_of_animal, birth_date, employee)
                    self.list_of_animals.append(new_animal)
                    employee.list_of_animals_to_take_care.append(
                        new_animal)  # ACA
                    return
                else:
                    print('Employee id does not exist')

    def create_employee(self):
        employee_id = input('Enter employee id: \n')
        name = input('Enter name of the employee: \n')
        last_name = input('Enter last name of the employee: \n')

        new_employee = Employee(employee_id, name, last_name)
        self.list_of_employees.append(new_employee)

    def print_employees(self):
        for employee in self.list_of_employees:
            employee.present_employee()

    def print_animals(self):
        for animal in self.list_of_animals:
            animal.present_animal()

    def change_employee(self):
        for animal in self.list_of_animals:
            animal.present_animal()
        name_animal = input(
            'Enter the name of the animal you want to change the caretaker for: \n')

        for animal in self.list_of_animals:
            if (name_animal == animal.name):
                for employee in self.list_of_employees:
                    employee.present_employee()
                new_employee_id = input(
                    'Enter the ID of the new caretaker you want to assign to the animal: \n')

                for employee in self.list_of_employees:
                    if (new_employee_id == employee.employee_id):
                        animal.assigned_employee = employee
                        employee.list_of_animals_to_take_care.append(animal)

    def assign_employee(self):
        employee_to_assign = input("Enter id of the employee to assign: ")
        for employee in self.list_of_employees:
            if employee_to_assign == employee.employee_id:
                animal_to_assign = input(
                    "Enter name of animal to assign new employee: ")
                for animal in self.list_of_animals:
                    if animal.name == animal_to_assign:
                        animal.assigned_employee = employee
                        print(
                            f"Employee {employee.employee_id} assigned to animal {animal.name}.")
                        return
    print("Employee or animal not found.")

    # change_animal and assign_employee basically have the same efect since you can only have one employee assign to an animal at the time
