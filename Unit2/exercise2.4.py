"""
Exercise 2.4:
The program should:

prompt the user to enter the current money of a person
prompt the user to enter the price of the input they want to buy in USD
convert that money to dollars (1USD -> 730$)
return True on the screen if they can buy, False if they cannot
There should be no errors
"""

ARS = ""
pri_usd = ""

print("""
Welcome to the currency converter. Currently, we only have one 
currency conversion available.
Please enter the keyword 'exit' to leave the converter
""")

while ARS.lower() != "out" and pri_usd.lower() != "out":
    try:
        ARS = (input("Available money (ARS): "))
        if ARS.lower() == "out":
            break
        pri_usd = (input("Input quantity (usd): "))
        if pri_usd.lower() == "out":
            break
        converter_usd = float(ARS) / float(pri_usd)
        if converter_usd >= 1:
            print(converter_usd >= 1)
            print(
                f"You can buy {converter_usd} usd with the available money")
        else:
            print(converter_usd >= 1)
            print("You can not buy usd")
    except ValueError as e:
        print("Insert numbers not text")
