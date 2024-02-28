"""

Exercise 7.10
Create a class called Employee with the following attributes:

name
age
position
Each time an object is created, the data must be saved in a JSON file with the format

"employees": [ {"name": employee1.name, "age": employee1.age, "position":
employee1.position}, ]

Create a class method that reads the information from the file and prints it in table format. Create a menu to create objects
"""

import json
import os


class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def return_dictionary(self):
        dictionary_ = {"name": self.name,
                       "age": self.age, "position": self.position}
        return dictionary_


employee_1 = Employee("jorge", 40, "manager")
employee_2 = Employee("jose", 25, "supervisor")

list_of_employees = [
    employee_1.return_dictionary(), employee_2.return_dictionary()]

dictionary = {"employees": list_of_employees}

try:
    file = open(
        f"{os.path.abspath(os.path.dirname(__file__))}//employees.json", "w")
    json.dump(dictionary, file)
    file.close()
except:
    print("File does not exist")
