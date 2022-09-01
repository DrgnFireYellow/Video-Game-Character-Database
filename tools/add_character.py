import json
with open("../db.json") as f:
    data = json.load(f)

name = input("Name of character: ")
description = input("Character description: ")

data[name] = {"description": description}
with open("../db.json", "w") as f:
    json.dump(data, f, indent=4)
