"""

The program must:

Have a Room class with the attributes (number (unique), max_people (int), price (float)).
Have two child classes that use the constructor of the parent class but have one more attribute:
StandardRoom (Attribute: num_tv (int)).
PremiumRoom (Attribute: Jacuzzi "True or False" (default = True)).

Create the following methods for the parent Room class (which will be inherited by the child classes):
Show information: Displaying the number, max_people, and price.
This method must be created in the parent class and the children, as the child classes must also display their attributes.
Set and get max_people.
Set and get price.
Obtain class type.




"""


class Room:
    def __init__(self, number, max_guests: int, price: float):
        self.number = number
        self.max_guests = max_guests
        self.price = price

    def print_info(self):
        print(
            f"Rooms: {self.number} - max_guests: {self.max_guests} - price: {self.price}")

    def max_guests_setter(self, guests):
        self.max_guests = guests

    def price_setter(self, price):
        self.price = price

    def type_of_room(self):
        print("I am a room of type: ", type(self).__name__)
        return type(self).__name__

    def get_max_guests(self):
        return self.max_guests


class Clasic(Room):
    def __init__(self, number, max_guests: int, price: float, amount_screens: int):
        super().__init__(number, max_guests, price)
        self.amount_screens = amount_screens

    def print_info(self):
        print(
            f"Room: {self.number} - max_guests: {self.max_guests} - price: {self.price} - TVs: {self.amount_screens}")


class Premium(Room):
    def __init__(self, number, max_guests: int, price: float, jacuzzi=True):
        super().__init__(number, max_guests, price)
        self.jacuzzi = jacuzzi

    def print_info(self):
        print(
            f"Room: {self.number} - max_guests: {self.max_guests} - price: {self.price} - jacuzzi: {self.jacuzzi}")
