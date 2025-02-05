class CardItem:
    discount_rate = 0.8
    item_count=0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CardItem.item_count+=1

    def calculate_total(self, p, q):
        return p * q

    def apply_discount(self, rate=None):  # rate'i opsiyonel yaptık
        if rate is None:  # Eğer rate verilmezse sınıfın discount_rate'ini kullan
            rate = CardItem.discount_rate
        self.price = self.price * rate


# Nesneleri oluştur
item1 = CardItem("Telefon", 50000, 2)
item2 = CardItem("Bilgisayar", 70000, 1)
item3 = CardItem("Kitap", 200, 2)

#Hem Class seviyesinde hem nesne seviyesinde ulaşılabilir.
print(CardItem.discount_rate)
print(item1.discount_rate)
print("*************")
print(CardItem.item_count)

#item 1'i dictionary olarak gösterme
print(item1.__dict__)
print(item2.__dict__)
print(item3.__dict__)
print(CardItem.__dict__)

# İndirim uygula
item1.apply_discount()
item2.apply_discount()
item3.apply_discount()

# Toplam fiyatları yazdır
print(item1.calculate_total(item1.price, item1.quantity))
print(item2.calculate_total(item2.price, item2.quantity))
print(item3.calculate_total(item3.price, item3.quantity))
