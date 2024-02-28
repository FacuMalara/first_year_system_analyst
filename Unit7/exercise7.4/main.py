"""

Exercise 7.4
Create a function to read a .csv file.

Create functions to:

Get the titles of each column (1st row).
Count the number of columns.
Count the number of rows.
"""


import os


def get_path():
    return os.path.abspath(os.path.dirname(__file__))


def open_csv(file_name):
    try:
        file_csv = open(f"{get_path()}//{file_name}", "r")
        text = file_csv.read()
        file_csv.close()
        return text
    except:
        print("File was not found")
        return ""


def get_titles():
    text = open_csv("mini_base.csv")
    titles = text.split("\n")
    column_titles = titles[0].split(",")
    print(column_titles)


def count_rows():
    text = open_csv("mini_base.csv")
    new_text = text.split("\n")
    count = 0
    for row in new_text:
        count += 1
    print(f"There are {count} rows in this text")


def count_columns():
    text = open_csv("mini_base.csv")
    new_text = text.split("\n")
    column_text = new_text[0].split(",")
    count = 0
    for columna in column_text:
        count += 1
    print(f"There are {count} columns in this text")


get_titles()
count_rows()
count_columns()
