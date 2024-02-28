"""
Exercise 2.3
The program should:

prompt the user to enter the age of a person
prompt the user to enter the years worked
return the years remaining until retirement (30 total years) and the
 age at which they would retire

"""
gender = input("Insert gender: ")
start = input("What age did you start to work: ")
age = input("Insert your age, integer numbers only: ")
y_worked = input("How many years did you work? Insert integer numbers: ")

if age.isnumeric and y_worked.isnumeric and start.isnumeric:
    age = int(age)
    y_worked = int(y_worked)
    start = int(start)
else:
    print("You tricked me")
if start <= 30:
    resting = 60 - 30 - start
else:
    resting = 0
if start <= 35:
    resting = 65 - 30 - start
else:
    resting = 0

retirement_age = age + (30 - y_worked) + resting
retirement_age = age + (30 - y_worked) + resting
to_work = retirement_age - age
to_work = retirement_age - age
if gender.lower() == "woman":
    print(f"You have {to_work} years until retirement")
elif gender.lower() == "man":
    print(f"You have {to_work} years until retirement")
