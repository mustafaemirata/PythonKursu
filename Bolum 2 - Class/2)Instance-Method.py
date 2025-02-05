class CardItem:
    def __init__(self,name, price, quantity):
        #instance attributes
        self.name=name
        self.price=price
        self.quantity=quantity

     # instance methods
    def calculate_total(self, p, q):
       return p * q
    def apply_discount(self,rate):
        self.price= self.price*(rate)

#instance => nesne, örnek
item1=CardItem("Telefon",50000,2)
item2=CardItem("Bilgisayar", 70000,1)
item3=CardItem("Kitap",200,2)

item1.apply_discount(0.8)
item2.apply_discount(0.7)
item3.apply_discount(0.9)

print(item1.calculate_total(item1.price,item1.quantity))
print(item2.calculate_total(item2.price,item2.quantity))
print(item3.calculate_total(item3.price,item3.quantity))