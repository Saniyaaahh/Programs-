class Item:
    def calculate_total_price(self, x, y):
        return x * y

item1 = Item()
item1_name = "Phone"
item1_price = 120
item1_quantity = 63
print(item1.calculate_total_price(item1_price, item1_quantity))


item2 = Item()
item2_name = "Laptop"
item2_price = 100
item2_quantity = 73
print(item2.calculate_total_price(item2_price, item2_quantity))


item3 = Item()
item3_name = "Iphone"
item3_price = 200
item3_quantity = 20
print(item3.calculate_total_price(item3_price, item3_quantity))