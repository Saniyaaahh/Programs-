class Item:

    pay_rate = 0.8 # payrate after 20% discount

    all = []
    def __init__(self, name: str, price: float, quantity=0):


        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_the_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"

item1 = Item("iphone", 500, 1)
item1.pay_rate = 0.5
item1.apply_discount()
print(item1.price)

item2 = Item("computer", 99, 1)
item2.apply_discount()
print(item2.price)


item3 = Item("mac", 4940, 1)
item3.apply_discount()
print(item3.price)

item4 = Item("samsung", 494, 1)
item5 = Item("helicopter", 899, 1)


#for instance in Item.all:
 #   print(instance.name)

print(Item.all)