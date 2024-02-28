import json
import os
try:
    file = open(
        f"{os.path.abspath(os.path.dirname(__file__))}//json_data", 'r')  # the load method doesn't work with other opening methods, for example "w", "+", "a"
    # read a json
    # load also doesn't accept sort_keys or indent arguments
    dictionary = json.load(file)
    file.close()
except:
    print("file does not exist")

print(dictionary)
