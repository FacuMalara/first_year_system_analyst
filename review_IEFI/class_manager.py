"""

Create instances of a room and store them in a room list.
1.1) It must be verified which type of Room instance to create and the parameters. IMPORTANT!: child classes verify and request parameters
- number: must be unique
- max_people: verify that it is an integer and is between 2 and 6 inclusive.
- price: must be requested in pesos but stored in dollars (1 dollar -> 900 pesos)
1.2) Child classes:
- num_tv: verify that it is an integer between 0 and 3 inclusive
- Jacuzzi: verify that it is True or False (boolean)

1.3) When creating a Room, it is necessary to log it (Write on a new line: number,max_people,price,class_type))
in a file called room_history.txt (Create function in the same manager). IMPORTANT!: verify permissions and extension

Change room price, selecting its number: The price of the room must be changed depending on the max number of
people it contains and the type of room:

The dictionary must be read by the room type and multiply that price by the number of people.
Eg. Standard room price = 400 (CL)* max_people = 400 * 5 = 2000 IMPORTANT! only ask the room number to the user
Ask the user for a number and list that number of rooms from the list, verifying that there are that number of rooms

The corresponding methods for the menu functions must be created in the corresponding classes
Manage possible errors
Structure the program at your own discretion
room_prices = {
"CO": 300,
"CL": 400,
"PR": 500
}
"""

from class_room import *


class RoomManager:
    def __init__(self):
        self.list_of_rooms: list[Room] = []

    def create_room(self):
        number = input("Number of the room: ")
        guests = input("Amount of guests: ")
        price = input("Enter price: ")
        text = f"{number}, {guests}, {price}"
        self.logear(text)

    def logear(self, text):
        try:
            file = open("log.csv", "a+")
            file.write(text + "\n")
            file.close()
        except:
            print("File not found")

    def change_price(self):
        price_of_rooms = {
            "Room": 300,
            "Clasic": 400,
            "Premium": 500
        }
        while True:
            number_of_room = input("Enter number of the room: ")
            for room in self.list_of_rooms:
                if room.number == number_of_room:
                    new_price = price_of_rooms.get(
                        room.type_of_room()) * room.get_max_guests()
                    room.price_setter(new_price)
                    print(new_price)
                    return
            print("Room does not exist")


manager = RoomManager()
manager.create_room()
manager.change_price()
