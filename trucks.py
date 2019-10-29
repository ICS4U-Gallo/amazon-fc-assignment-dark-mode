class Incoming_trucks:
    """Incoming trucks class

    Attributes:
        clothing (str): clothes
        electronics (str): any electronic device
        automotive (str): parts for automobiles
        home_kitchen (str): appliances for a home and kitchen
        sports (str): sports apparel and equipment
        tools (str): tools for handyman things
        toys_game (str): games and toys
    """
    def __init__(self, clothing, electronics, automotive, home_kitchen, 
    sports, tools, toys_games):
        """Create an incoming truck object"""
        self.clothing = clothing
        self.electronics = electronics
        self.automotive = automotive
        self.home_kitchen = home_kitchen
        self.sports = sports
        self.tools = tools
        self.toys_game = toys_games


class Outgoing_trucks:
    """Outgoing trucks class

    Attributes:
        short_distance (str): trucks travelling a short distance
        med_distance (str): trucks travelling a medium distance
        long_distance (str): trucks travelling a long distance
    """
    def __init__(self, short_distance, med_distance, long_distance):
        """Create and outgoing truck object

        Args:
            short_distance (str): trucks travelling a short distance
            med_distance (str): trucks travelling a medium distance
            long_distance (str): trucks travelling a long distance
        """
        self.short_distance = short_distance
        self.med_distance = med_distance
        self.long_distance = long_distance
