"""Import data from database_storage.pickle"""
with open("database_storage.pickle", "rb") as f:
    database = pickle.load(f)


class Package:
    """Package class

    Attributes:
        item (str): the type of item being packaged
        size (str): size of the package
        address (str): where the package is being shipped 
    """
    def __init__(self, item: str, size: str, address: str):
        """Create a package object

        Args:
            item: item being packaged
            size: size of the package
            address: where the package is being shipped
        """
        self.item = item
        self.size = size
        self.address = address

    for i in database[item_type]:
        if database[i].name == user_item:
            index = i

    item_size = database[index].size

    def ouptut_info_to_trucks():       
        output_to_trucks = "Sending, {} package with {} to {}".format(item_size, index, address)
        database[item_type].pop(index)
        return output_to_trucks
