import pickle
from trucks import *


class Item:
  def __init__(self, name, size, item_type):
    self.name = name
    self.size = size
    self.item_type = item_type


def main():
    user_input = int(input("Clear Database: 1\nDefault Test Items: 2"))

    if user_input == 1:
        with open("database_storage.pickle", "rb") as f:
            database = pickle.load(f)

        database = {"clothing":[], "electronics":[], "automotive":[], "home_kitchen":[], "sports":[], "tools":[], "toy_game":[]}

        with open("database_storage.pickle", "wb") as f:
            pickle.dump(database, f, protocol=pickle.HIGHEST_PROTOCOL)

    elif user_input == 2:
            with open("database_storage.pickle", "rb") as f:
                database = pickle.load(f)

            item1 = Item("Tee-Shirt", "small", "clothing")
            item2 = Item("Gucci Belt", "small", "clothing")
            item3 = Item("Iphone X", "small", "electronics")
            item4 = Item("Charger", "small", "electronics")
            item5 = Item("Literal Car Engine", "large", "automotive")
            item6 = Item("Windex", "small", "automotive")
            item7 = Item("Crafting Table", "medium", "home_kitchen")
            item8 = Item("Oven", "large", "home_kitchen")
            item9 = Item("Duffel Bag", "medium", "sports")
            item10 = Item("Football", "small", "sports")
            item11 = Item("Swiss Army Knife", "small", "tools")
            item12 = Item("Power Drill", "medium", "tools")
            item13 = Item("Nintendo 64", "medium", "toy_games")
            item14 = Item("Cards", "small", "toy_games")

            truck = Incoming_trucks([item1, item2], [item3, item4], [item5, item6], [item7, item8],
                     [item9, item10], [item11, item12], [item13, item14])

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