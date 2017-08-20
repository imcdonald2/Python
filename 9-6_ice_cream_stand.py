class Restaurant():
    """Restaurant open signs"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine."""
        self.name = restaurant_name
        self.food = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " serves delicious " + self.food + ".")

    def open_restaurant(self):
        print(self.name.title() + " is now open.")

class IceCreamStand(Restaurant):
    """A simple attempt to represent an Ice Cream Stand"""
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.name = restaurant_name
        self.food = cuisine_type
        self.flavors = "chocolate, vanilla, strawberry"

    def describe_flavors(self):
        print("We currently only have " + self.flavors + " ice cream.")

friendlies = IceCreamStand("Friendlys")
friendlies.describe_restaurant()
friendlies.describe_flavors()
