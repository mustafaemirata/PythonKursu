class CardItem:
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

item1=CardItem("Telefon",50000,2)


item2=CardItem("Bilgisayar", 70000,1)


print(item1.name)
print(item2.name)