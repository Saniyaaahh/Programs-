class Bakery:

    pay_rate = 0.8 # payrate after 20% discount

    all = []
    def __init__(self, name: str, price: float, quantity=0):


        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Bakery.all.append(self)

    def calculate_the_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"

item1 = Bakery("osmania", 40, 500)
item2 = Bakery("cake", 300, 35)
item3 = Bakery("pastry", 25, 40)
item4 = Bakery("puff", 15, 50)
item5 = Bakery("sandwhich", 35, 20)
item6 = Bakery("bun", 12, 4)
item7 = Bakery("pizza", 200, 9)
item8 = Bakery("roll", 50, 7)


for instance in Bakery.all:
    print(instance.name ,instance.price, "rupees each")

print(item2.calculate_the_price())
