import os
import csv

with open(f"{os.path.abspath(os.path.dirname(__file__))}//mini_base(1).csv") as file:
    # csv.reader(file,delimiter = ";")
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        # print(row)
        print(f"{row[0]} - {row[1]} - {row[2]}")
