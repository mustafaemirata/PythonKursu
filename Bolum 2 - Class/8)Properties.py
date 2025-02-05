class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = None
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Ürün fiyatı negatif değer alamaz.")

p = Product("Iphone 16", 80000)
p.price = 90000  # Setter metodu çalışıyor
print(p.name, p.price)  # Çıktı: Iphone 16 90000

p=Product("Iphone 16",80000)
p.set_price(90000)
print(p.name, p.price)

