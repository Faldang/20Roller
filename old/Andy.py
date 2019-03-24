import csv
import json

a = input("unesi poop:\n")
print(a)

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
        }
    }

json_string = json.dumps(data, indent=4)
print(json_string)
