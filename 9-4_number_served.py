class Restaurant():
    """Describe the Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name: " + self.name)
        print("Cuisine Type: " + self.food)

    def open_restaurant(self):
        """Prints that the restaurant is open"""
        print(self.name + " is now open.")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, customers):
        self.number_served += customers

restaurant = Restaurant('Applebees', 'garbage')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.set_number_served(5)
restaurant.increment_number_served(10)
print(restaurant.number_served)
