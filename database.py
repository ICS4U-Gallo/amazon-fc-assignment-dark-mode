import json


with open("database_storage.json", "r") as f:
    database = json.load(f)




with open("database_storage.json", "w") as f:
    json.dump(database, f)
