import json

with open("embassament.json", mode="r", encoding="utf-8") as file:
    list = json.loads(file.read())

print(list) # list of dictionaries

