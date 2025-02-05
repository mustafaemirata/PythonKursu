class CardItem:
    discount_rate = 0.8
    item_count=0
    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."

    @classmethod

    def create_item(cls,data_str):
        name,price,quantity=data_str.split(",")
        return cls(name,price,quantity)
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CardItem.item_count+=1

    def calculate_total(self, p, q):
        return p * q

    def apply_discount(self):
        self.price = self.price * CardItem.discount_rate

print(CardItem.display_item_count())
# Nesneleri oluştur
item1 = CardItem("Telefon", 50000, 2)
item2 = CardItem("Bilgisayar", 70000, 1)
print(CardItem.display_item_count())
item3 = CardItem("Kitap", 200, 2)
print(CardItem.display_item_count())

CardItem.create_item("Mouse, 800,3")
print(CardItem.display_item_count())





