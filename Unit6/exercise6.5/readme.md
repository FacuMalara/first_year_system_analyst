
###Exercise 6.5
Create a parent class Computer:

The constructor must include the attributes (id_model, peripheral_list, OS, brand).
Create methods for this class:

1. Introduce yourself (id_model, peripheral_list, OS).
2. Indicate type of Computer (Inherited classes).
3. Methods that will later modify the child classes. add_peripherals, ChangeOS.

Create 2 classes that inherit from the parent class Computers, with a particular attribute for each one:

1. Desktop
2. Laptop

Create a ComputerManager class that has the following functions for a menu:

1. Create Computer, indicating type and save in a list. Verifying brand and OS from a list.
2. List Computers (presenting them), indicating type.
3. Change OS of a Computer, verifying a list of available OS.
4. List peripherals.