# Import the module
import json
import os

# JSON-formatted string
json_data = """
{
	"size": "medium",
	"price": 15.67,
	"toppings": ["mushrooms", "extra cheese", "pepperoni", "basil"],
	"customer": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}
"""

# Convert JSON-formatted string to a dictionary
data_dictionary = json.loads(json_data)
print(data_dictionary["price"])
