import json

with open("../db.json") as f:
    data = json.load(f)

for character in data:
    print()
    print(character)
    for value in data[character]:
        print(f"{value}: {data[character][value]}")
    print()