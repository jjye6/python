import json

with open("embassament.json", mode="r", encoding="utf-8") as file:
    list_dicc = json.loads(file.read())

print(list_dicc) # list of dictionaries

