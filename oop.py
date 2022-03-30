# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))

class Item:
    # class attributes (pay_rate)
    pay_rate = 0.8  # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        # print(f"An instance created: {name}")
        # Run validations to the received args
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # cant access the pay_rate directly have to use Item.pay_rate


item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)
print(Item.pay_rate)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.pay_rate)
print(item2.calculate_total_price())
item3 = Item("Laptop", 12)

print(item1.calculate_total_price())
# print(Item.__dict__)  # All the attributes for class level
# print(item1.__dict__)   # All the attributes for instance level


print(item3.calculate_total_price())