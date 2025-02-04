sayilar=[1,2,3,4,5,6]
sayilar_str=["1","3","8","4"]
isimler=["ali","ayşe","zeynep","hasan"]
kullanicilar=[
    {"ad":"ali","soyad": "yılmaz"},
    {"ad": "ahmet","soyad":"cengiz"}
]
#kareleri=[]
#for sayi in sayilar:
#    kareleri.append(sayi**2)
#print(kareleri)

def kareAl(sayi):
    return sayi**2
sonuc2=list(map(lambda sayi:sayi**2,sayilar))
sonuc3=list(map(int,sayilar_str))
sonuc=list(map(str.capitalize,isimler))
sonuc=list(map(lambda kisi: kisi["ad"],kullanicilar))
print(sonuc)
print(sonuc2) #adres verir. List eklenirse değeri verir.
print(sonuc3)