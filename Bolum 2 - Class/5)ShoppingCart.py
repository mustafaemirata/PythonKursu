class CardItem:
    discount_rate = 0.8
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."

    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name, float(price), int(quantity))  # Tip dönüşümü ekledim

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)  # Sayısal değer olarak kaydedelim
        self.quantity = int(quantity)
        CardItem.item_count += 1

    def apply_discount(self):
        self.price = self.price * CardItem.discount_rate


# Ürünleri oluştur
item1 = CardItem("Telefon", 50000, 2)
item2 = CardItem("Bilgisayar", 70000, 1)
item3 = CardItem("Kitap", 200, 2)


class Cupon:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount


# Kuponları oluştur
c1 = Cupon("code1", 0.8)
c2 = Cupon("code2", 0.75)
c3 = Cupon("code3", 0.9)


class ShoppingCart:
    cupon_list = [c1, c2, c3]

    def __init__(self, liste):
        self.liste = liste

    def add_item(self, item):
        self.liste.append(item)

    def display_item(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")

    def calculate_total(self):
        return sum([item.price * item.quantity for item in self.liste])  # Hata düzeltildi

    def remove_item(self, cart_item):
        self.liste = [item for item in self.liste if item != cart_item]

    def clear(self):
        self.liste = []

    @classmethod
    def get_coupons(cls):
        return cls.cupon_list

    @classmethod
    def get_coupon(cls, code):
        return next((c for c in cls.cupon_list if c.code == code), None)

    def apply_coupon(self, code):
        cupon = ShoppingCart.get_coupon(code)

        if not cupon:
            raise ValueError(f"Geçersiz kupon! {code}")

        for item in self.liste:
            item.price = item.price * cupon.discount  # Fiyatı indirime uygula


# Alışveriş sepetini oluştur
sc = ShoppingCart([item1, item2])
sc.add_item(item3)

sc.display_item()
print("---------")

sc.remove_item(item1)
sc.display_item()

# Kupon uygula
try:
    sc.apply_coupon("code2")
    print("Kupon uygulandı!")
except ValueError as e:
    print(e)

print("Toplam Fiyat:", sc.calculate_total())
