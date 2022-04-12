from item import Item
from phone import Phone


Phone1 = Phone("Iphone", 12200, 30, 2)
print(Phone1.calculate_total_price())
print(Item.is_integer(3.0))
Item.instantiate_from_csv()
print(Phone1.name)
Phone1.name = "OurPhone"
Phone1.apply_increment(0.2)
print(Phone1.price)
print(Item.all)
print(Phone.all)