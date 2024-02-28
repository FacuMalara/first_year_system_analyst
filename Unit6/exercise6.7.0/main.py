'''
Simulate a zoo animal management program, which has two classes: Animals and Employees.

The Animals class has the attributes (name, animal_type, date_of_birth, caretaker (Name of employee object)).

Create 3 classes that inherit from Animals according to their zoo sector:

1. Animals in cages.
2. Free-roaming animals.
3. Aquatic animals.

The Employees class has the attributes (ID, first_name, last_name, list_of_animals_to_care_for (Animal class)).
An employee can care for animals from different sectors.

Have 6 functions available in the menu (these functions should be included in a class called ZooManager):

1. Create instances of animals (you can choose between the three sectors) and save them in a list.
2. Create an instance of Employees and save them in a list.
    Employees can be assigned animals later; the animals when created in the system must have a caretaker.
3. Assign an animal to an employee to care for.
4. Change the caretaker of an animal.
5. Print a list of animals (with all their information).
6. Print a list of Employees (with all their information).

The corresponding methods for the menu functions should be created in the respective classes.

Manage potential errors.

Structure the program according to your own criteria.'''


from zoo_manager import *
manager = ZooManager()

while True:
    menu = '''

-----------------------MAIN MENU-----------------------

1. Create animal
2. Create employee
3. Change the caretaker of an animal
4. Assign employee to an animal
5. Print list of animals
6. Print list of employees
7. Exit

Enter an option: '''

    option = input(menu)
    if (option == '1'):
        manager.create_animal()
    elif (option == '2'):
        manager.create_employee()
    elif (option == '3'):
        manager.change_employee()
    elif (option == '4'):
        manager.assign_employee()
    elif (option == '5'):
        manager.print_animals()
    elif (option == '6'):
        manager.print_employees()
    elif (option == '7'):
        exit()
    else:
        print('Incorrect option')
