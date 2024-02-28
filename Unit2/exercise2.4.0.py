"""
Exercise 2.4:
The program should:

prompt the user to enter the current money of a person
prompt the user to enter the price of the input they want to buy in USD
convert that money to dollars (1USD -> 730$)
return True on the screen if they can buy, False if they cannot
There should be no errors

This is another way to solve the exercise
"""

ARS = ""
pre_usd = ""

print("""

"Welcome to the currency converter. Currently, we only have one 
currency conversion available.
Please enter the keyword 'exit' to leave the converter."
""")

while ARS.lower() != "out" and pre_usd.lower() != "out":
    try:
        ARS = (input("Available money (ARS): "))
        if ARS.lower() == "out":
            break
        while not ARS.isnumeric() and ARS.lower() != "out":
            print("Invalid income")
            ARS = (input("Available money (ARS): "))
        if ARS.lower() == "out":
            break
        pre_usd = (input("Insert amount (usd): "))
        if pre_usd.lower() == "out":
            break
        while not pre_usd.isnumeric() and pre_usd.lower() != "out":
            print("Invalid data")
            pre_usd = (input("Insert available money (usd): "))
        if pre_usd.lower() == "out":
            break
        converter_usd = float(ARS) / float(pre_usd)
        if converter_usd >= 1:
            print(converter_usd >= 1)
            print(
                f"You can buy {converter_usd} usd with this amount of ARS")
        else:
            print(converter_usd >= 1)
            print("Not possible to buy")
    except ValueError as e:
        print("Only numbers, not text")
