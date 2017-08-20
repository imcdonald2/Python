class Restaurant():
    """Describe the Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name: " + self.name)
        print("Cuisine Type: " + self.food)

    def open_restaurant(self):
        """Prints that the restaurant is open"""
        print(self.name + " is now open.")

restaurant = Restaurant('Applebees', 'garbage')
restaurant.describe_restaurant()
restaurant.open_restaurant()
