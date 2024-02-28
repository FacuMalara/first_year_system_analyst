import os
import json

with open(f"{os.path.abspath(os.path.dirname(__file__))}//json_data", "r") as file:
    data_dict = json.load(file)
    print(data_dict)
