"""
Create a ComputerManager class that has the following functions for a menu

1. Create Computer, indicating type and save in a list. Verifying brand and OS from a list
2. List Computers (presenting them), indicating type.
3. Change OS of a Computer, checking a list of available OS
4. List peripherals"""

from computer import *


class ComputerManager:
    # Class atributes
    list_of_brands = ['dell', 'hp', 'apple']
    list_SO = ['macOS', 'linux', 'windows']

    def __init__(self):
        self.list_of_computers: list[Computer] = []

    def ask_type(self):
        while True:
            print('------ Posible pcs to create ------')
            class_type = input('Enter pc type: ')
            for i in Computer.__subclasses__():
                if i.__name__ == class_type:
                    return class_type
            print('That class does not exist')

    def require_brand_SO(self, object_to_be_required, list_of_objects):
        while True:
            print(f'------ Posible {object_to_be_required} to create ------')
            for obj in list_of_objects:
                print(f'- {obj}')
            obj = input(f'Enter the {object_to_be_required}: ')
            if obj in list_of_objects:
                return obj
            else:
                print(f' {object_to_be_required} does not exist')

    def require_periferics_list(self):
        periferic_list = []
        while True:
            periferic = input(
                'Enter periferic to add ("exit" to finish): ')
            if periferic == 'exit':
                return periferic_list
            else:
                periferic_list.append(periferic)

    def create_computer(self):
        class_type = self.ask_type()
        id = input('Enter id: ')
        brand = self.require_brand_SO('brand', self.list_of_brands)
        so = self.require_brand_SO('SO', self.list_SO)
        periferic_list = self.require_periferics_list()
        if class_type == 'Notebook':
            weight = input('Enter weight: ')
            object_pc = Notebook(id, periferic_list, so, brand, weight)
        if class_type == 'Desktop':
            cables = input('Enter amount of cables:')
            object_pc = Desktop(id, periferic_list, so, brand, cables)

        self.list_of_computers.append(object_pc)

    def list_computers(self):

        # for pc in self.lista_computadoras:
        #    for i in Computadora.__subclasses__():
        #        if i.__name__ == str(type(pc)):
        #            pc.get_tipo()
        #            subclass_obj = pc.index(pc.marca+1)
        #            print(
        #                F"Este tipo de clase se diferencia por el atributo {subclass_obj}")

        for pc in self.list_of_computers:
            pc.get_type()

    def change_SO(self):
        id = input("Enter id of the computer: ")
        for computer in self.list_of_computers:
            if computer.id_model == id:
                new_SO = self.require_brand_SO("SO", self.list_SO)
                computer.SO = new_SO
                computer.get_type()
            else:
                print("Computer does not exist")

    def list_periferics(self):
        print("----Periferics----")
        counter = 0
        for computer in self.list_of_computers:
            counter = +1
            print(
                f"Computer {counter}- Id:{computer.id_model}\nPeriferics:")
            for periferic in computer.periferic_list:
                print(f"{counter}. {periferic} ")
