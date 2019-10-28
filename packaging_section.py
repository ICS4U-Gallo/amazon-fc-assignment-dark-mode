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

    def get_package(self): 
        pass  

    def add(self, item):
        item.oven = self.item
        item.size = self.size
        item.address = self.address

    
    
    
    
