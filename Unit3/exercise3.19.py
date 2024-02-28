"""

Exercise 3.19
The program should:

Ask the user for an amount of money to invest
Ask the user for the annual interest rate and the number of years
Display on the screen the capital obtained in the investment for 
each year the investment lasts.
"""

try:
    money = float(input("Enter amount available to invest: "))
    interest = float(input("Enter annual interest: "))
    years = int(input("Enter amount of years: "))

    for year in range(years):
        years += 1                           # if years = 0 there is no interest
        annual_result = money * interest
        money = money + annual_result
        print(money)
except ValueError as e:
    print(f"Error: {e}")
