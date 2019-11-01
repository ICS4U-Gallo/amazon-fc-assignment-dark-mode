import pickle
from temporary_database_reset import Item

with open("database_storage.pickle", "rb") as f:
    database = pickle.load(f)


def item_selection(select):
    print("These are the items that are available:")
    for items in database[select]:
        print('--->{}'.format(items.name))
    print("Which one would you like to purchase?")
    while True:
        try:
            selected = int(input("Please input a number according to the list, "
                                 "for example:\nFish\nChips\nFish = 0,Chips = 1, or enter -1 to go back: "))
            if selected >= 0:
                return database[select][selected]
                break
            elif selected < 0:
                makeshiftapi()
                break
        except ValueError:
            print("That's not a valid number")


def send_to_package(item):
    print('Please enter the information required')
    name = input('Name: ')
    address = input('Address: ')
    pass


def makeshiftapi():
    print("Hi, which section would you life to browse today?")

    for i, o in database.items():
        print(i)
    while True:
        selection = input("Please enter your selection here from the list above: ")
        if selection.lower() == "toy_game" or selection.lower() == "toy game":
            item_selection('toy_game')
            break
        elif selection.lower() == "home_kitchen" or selection.lower() == "home kitchen":
            item_selection('home_kitchen')
            break
        elif selection.lower() == "tools":
            item_selection('tools')
            break
        elif selection.lower() == "electronics":
            item_selection('electronics')
            break
        elif selection.lower() == "automotive":
            item_selection('automotive')
            break
        elif selection.lower() == "clothing":
            item_selection('clothing')
            break
        elif selection.lower() == "sports":
            item_selection('sports')
            break
        else:
            print("That is not a valid selection")



if __name__ == "__main__":
    makeshiftapi()