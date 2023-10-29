class Item:
    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_the_price(self):
        return self.price * self.quantity

item1 = Item("iphone", 500, 2)
item2 = Item("computer", 499, 3)

print(item2.calculate_the_price())