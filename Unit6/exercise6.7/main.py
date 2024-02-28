from animal_manager import *


def main():

    obj_manager = ZooManager()

    while True:
        menu = input("""

1. Create animal instances (you can choose between the three sectors) and save them in a list
2. Create an instance of Employees and save them in a list
    * Employees can be assigned animals later, the animals when created in the system must have a caretaker assigned
3. Assign an animal to an employee to care for
4. Change the caretaker of an animal
5. Print list of animals (with all their information)
6. Print list of Employees (with all their information)
7. Exit
                     
Insert option: 
""")

        if menu == '1':
            obj_manager.create_animal()
        elif menu == '2':
            obj_manager.create_employee()
        elif menu == '3':
            obj_manager.assign_animal()
        elif menu == '4':
            obj_manager.change_animals_employee()
        elif menu == '5':
            obj_manager.print_list_of_animals()
        elif menu == "6":
            obj_manager.print_list_of_employees()
        elif menu == "7":
            print("Ending process")
            break
        else:
            print('Incorrect income')


if __name__ == "__main__":
    main()

# This exercise is incomplete and has mistakes
