"""

Student: Malara Facundo

Exercise 3.4
Federico Bosack
•
24 Aug
100 points
Deadline: 31 Aug, 23:59
The program should:

Store a variable password with a password
Ask the user for the password and
print on the screen if the password
entered by the user matches or not with the variable
IMPORTANT: without considering uppercase and lowercase letters. (string methods)
should not generate errors
Solution:
"""

password = input("Enter password please: ")

if password.lower() == "tarambana":
    print("Entered password matches with variable 'password'")
else:
    print("Entered password does not match with variable 'password'")
