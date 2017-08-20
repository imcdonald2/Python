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
