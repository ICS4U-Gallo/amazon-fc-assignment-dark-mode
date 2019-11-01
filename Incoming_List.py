class Incoming_List:
    List = {}
    def __init__(self, clothing, electronics, automotive, home_kitchen, 
    sports, tools, toys_games):  
        """ Add two numbers.

        Arg:
            clothing: An clothing item
            electronics: An electronics item
            automotive: An automotive item
            home_kitchen: An home_kitchen item
            sports: An sports item
            tools: An tools item
            toys_games: An toys_games item

        Returns:
            clothing: An clothing dict
            electronics: An electronics dict
            automotive: An automotive dict
            home_kitchen: An home_kitchen dict
            sports: An sports dict
            tools: An tools dict
            toys_games: An toys_games dict
        """

        self.clothing = clothing
        self.electronics = electronics
        self.automotive = automotive
        self.home_kitchen = home_kitchen
        self.sports = sports
        self.tools = tools
        self.toys_games = toys_games
        List = {
                "clothing": self.clothing, 
                "electronics": self.electronics, 
                "automotive": self.automotive, 
                "home_kitchen": self.home_kitchen, 
                "sports": self.sports, 
                "tools": self.tools, 
                "toys_games": self.toys_games, 
                }
    def get_clothing():
        return List["clothing"]
    
    def get_electronics():
        return List["electronics"]
    
    def get_automotive():
        return List["automotive"]  
    
    def get_home_kitchen():
        return List["home_kitchen"]
    
    def get_sports():
        return List["sports"]
    
    def get_tools():
        return List["tools"]
    
    def get_toys_games():
        return List["toys_games"]

