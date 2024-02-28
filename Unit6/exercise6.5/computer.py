"""
Create a parent class Computer:

The constructor should include attributes (id_model, peripherals_list, OS, brand).
Create methods for this class:

1. Present (id_model, peripherals_list, OS).
2. Indicate type of Computer (Inherited classes).
3. Methods that will later modify the child classes. add_peripherals, change_OS.

Create 2 classes that inherit from the parent class Computers, with a particular attribute for each one:

1. Desktop
2. Laptop
"""


class Computer:
    # id_model: str
    def __init__(self, id_model: str, periferic_list: list, SO: str, brand: str):
        self.id_model = id_model
        self.periferic_list = periferic_list
        self.SO = SO
        self.brand = brand

    def get_type(self):
        print(
            f'I am a computer of type: {type(self).__name__}, {self.id_model}, {self.periferic_list}, {self.SO}, {self.brand}')

    def add_periferics(self):
        pass

    def change_so(self):
        pass


class Desktop(Computer):
    def __init__(self, id_model: str, periferic_list: list, SO: str, brand: str, amount_cables: str):
        super().__init__(id_model, periferic_list, SO, brand)
        self.amount_cables = amount_cables


class Notebook(Computer):
    def __init__(self, id_model: str, periferic_list: list, SO: str, brand: str, weight: str):
        super().__init__(id_model, periferic_list, SO, brand)
        self.weight = weight
