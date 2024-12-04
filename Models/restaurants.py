class Restaurant():
    restaurants_list = []
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.active = False
        Restaurant.restaurants_list.append(self)

    def __str__(self):
        return f'{self.name} | {self.cuisine}'

    def list_restaurants(self):
        for restaurant in Restaurant.restaurants_list:
            print(f'{restaurant.name} | {restaurant.cuisine} | {"Active" if restaurant.active else "Inactive"}')  

restaurant_sushi = Restaurant('Flying Sushi', 'Japanese')
restaurant_mcdonalds = Restaurant('McDonalds', 'Fast Food')
restaurant_king = Restaurant('King', 'Italian')

Restaurant.list_restaurants()