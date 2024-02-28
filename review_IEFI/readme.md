
'''

SUBJECT: Algorithms and Data Structures 1
LAST NAME AND NAME:
ID NUMBER:
CAREER:

Items to evaluate:

Subject contents
Requirements and understanding of instructions
Structure (modularization), readability, and code comments.
Any questions about the statement, consult the teacher!

STATEMENT: "Hotel Management Program"

Introduction:
The following program consists of software that simulates a program to manage the rooms of a hotel.
The program should allow adding and removing rooms from the system, as well as managing data for these (number, max_persons, price).

Requirements:
The program must:

Have a Room Class with the attributes (number (unique), max_people (int), price (float))

Have two Child Classes that use the constructor of the parent class but have one more attribute:
- StandardRoom (Attribute: num_tv (int))
- PremiumRoom (Attribute: Jacuzzi "True or False" (default = True))

The following methods must be created for the parent Room class (which will be inherited by the child classes):
1. Show information: Displaying the number, max_people, and price
- This method must be created in the parent class and the children, as the child classes must also display their attributes
2. Set and get max_people
3. Set and get price
4. Obtain class type

Create a RoomManager class that has the following functions for a menu:

Create instances of a room and store them in a room list.
1.1) It must be verified which type of Room instance to create and the parameters. IMPORTANT!: child classes verify and request parameters
- number: must be unique
- max_people: verify that it is an integer and is between 2 and 6 inclusive.
- price: must be requested in pesos but stored in dollars (1 dollar -> 900 pesos)
1.2) Child classes:
- num_tv: verify that it is an integer between 0 and 3 inclusive
- Jacuzzi: verify that it is True or False (boolean)

1.3) When creating a Room, it is necessary to log it (Write on a new line: number, max_people, price, class_type))
in a file called room_history.txt (Create function in the same manager). IMPORTANT!: verify permissions and extension

Change room price, selecting its number: The price of the room must be changed depending on the max number of
people it contains and the type of room:

The dictionary must be read by the room type and multiply that price by the number of people.
Eg. Standard room price = 400 (CL)* max_people = 400 * 5 = 2000 IMPORTANT! only ask the room number to the user
Ask the user for a number and list that number of rooms from the list, verifying that there are that number of rooms

The corresponding methods for the menu functions must be created in the corresponding classes

Manage possible errors

Structure the program at your own discretion
'''
room_prices = {
"CO": 300,
"CL": 400,
"PR": 500
}




Incomplete exercise