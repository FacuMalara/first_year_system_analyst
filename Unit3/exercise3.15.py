"""
Exercise 3.15
The following program shows the color obtained
by mixing two colors on the screen,
with the 3 possibilities being:

Blue
Red
Green
"""

print("Welcome to the mixer, if you want to exit, type 'exit'")
primary_color = ""
secondary_color = ""
flag = True

while flag:
    while True:
        primary_color = input("Choose a colour, 'g' 'r' 'y': ")
        if primary_color.lower() == "out":
            break
        if primary_color.lower() != "g" and primary_color.lower() != "r" and primary_color.lower() != "y":
            print("Enter two different colours")
        else:
            break

    while primary_color.lower() != "out":
        secondary_color = input("Choose other colour: ")
        if secondary_color.lower() == "out":
            break
        if secondary_color.lower() != "g" and secondary_color.lower() != "r" and secondary_color.lower() != "y":
            print("Invalid, insert other colour 'g' 'r' 'y': ")
        if secondary_color.lower() == primary_color.lower():
            print("Invalid, enter two different colours")
        else:
            break

    while primary_color.lower() != "out" and secondary_color.lower() != "out":
        if (primary_color.lower() == "y" or primary_color.lower() == "g") and (secondary_color.lower() == "g" or secondary_color.lower() == "y"):
            result = "Cyan"
        elif (primary_color.lower() == "r" or primary_color.lower() == "g") and (secondary_color.lower() == "g" or secondary_color.lower() == "r"):
            result = "Yellow"
        else:
            result = "Purple"
        print(result)
        break
    if primary_color.lower() == "out" or secondary_color.lower() == "out":
        flag = False
