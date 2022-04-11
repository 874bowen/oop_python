from item import Item
from phone import Phone


Phone1 = Phone("Iphone", 12200, 30, 2)
print(Phone1.calculate_total_price())
print(Item.is_integer(3.0))
Item.instantiate_from_csv()
print(Phone1.name)
print(Item.all)
print(Phone.all)