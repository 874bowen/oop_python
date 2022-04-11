import csv


class Item:
    # class attributes (pay_rate)
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to the received args
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self._name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # cant access the pay_rate directly have to use Item.pay_rate

    @classmethod # decorator to say that it is not a class function
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
                 )
            print(item)

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
