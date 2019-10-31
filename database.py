import json
import pickle
from trucks import *

class Item:
  def __init__(self, name, size, item_type):
    self.name = name
    self.size = size
    self.item_type = item_type

with open("database_storage.pickle", "rb") as f:
    database = pickle.load(f)

for item in truck.clothing:
    database["clothing"].append(item)
for item in truck.electronics:
    database["electronics"].append(item)
for item in truck.automotive:
    database["automotive"].append(item)
for item in truck.home_kitchen:
    database["home_kitchen"].append(item)
for item in truck.sports:
    database["sports"].append(item)
for item in truck.tools:
    database["tools"].append(item)
for item in truck.toys_game:
    database["toy_game"].append(item)

with open("database_storage.pickle", "wb") as f:
    pickle.dump(database, f, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    main()
