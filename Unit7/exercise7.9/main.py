'''
Exercise 7.9
Create a Python program that reads the JSON file (students.json) and prints the following information for each student:

Student's name.
Student's age.
List of subjects they are studying.'''

import json
import os
try:
    file = open(
        f"{os.path.abspath(os.path.dirname(__file__))}//students.json", 'r')
    # leer un json
    dictionary = json.load(file)
    file.close()
except:
    print("File does not exist")

for student in dictionary["students"]:
    print(
        f"Students: {student.get('name',None)} - age: {student['age']} - subjects: {student['subjects']}")
