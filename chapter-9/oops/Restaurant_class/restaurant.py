class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 
    
    def describe_restaurant(self):
        print(f" the {self.restaurant_name} has a special cusine called {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")

        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = "vinnela"
    
    def get_icecream(self):
        print(f" here is your {self.cuisine_type} with {self.flavors} flavor hope you like it")
    
    def update_flavour(self,flavors):
        self.flavors = flavors