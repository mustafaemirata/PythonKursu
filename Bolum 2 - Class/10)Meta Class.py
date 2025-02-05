class BaseClass:
    def show(self):
        return "Merhaba"

# Yeni metod ekleme fonksiyonu
def add_attribute(self):
    self.b = 10  # `b` değişkenini dinamik olarak ekle

# type() ile dinamik sınıf oluşturma
Test = type("Test", (BaseClass,), {"a": 5, "add_attribute": add_attribute})  # Parantez yok!

t = Test()

# Test sınıfının miras aldığı methodu çağırıyoruz
sonuc = t.show()  # "Merhaba"

# Dinamik olarak eklenen `a` değişkenini çağırıyoruz
sonuc_a = t.a  # 5

# `add_attribute` fonksiyonunu çağırarak `b` değişkenini ekliyoruz
t.add_attribute()
sonuc_b = t.b  # `b` değişkeni artık var!

print(sonuc)   # Çıktı: Merhaba
print(sonuc_a) # Çıktı: 5
print(sonuc_b) # Çıktı: 10
print("--------------------------------")

class Meta(type):
    def __new__(sef, class_name,bases,attrs):
        print(attrs)
        a={}

        for name, val in attrs.items():
            if name.startswith("_"):
                a[name]=val
            else:
                a[name.upper()]=val
        return type(class_name,bases,a)

        return type(class_name,bases,attrs)
class Person(metaclass=Meta):
    x=5
    y=10
    _AGE=83

    def hello(self):
        print("Merhaba!")
#Sahip olduğu attributeleri yazdırdık.
p=Person()
sonuc=p._AGE
sonuc=p.X
print(sonuc)
