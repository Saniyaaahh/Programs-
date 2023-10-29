class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_the_price(self):
        return self.price * self.quantity

item1 = Item("iphone", 500, 5)
item2 = Item("computer", 499, 3)

print(item2.calculate_the_price())