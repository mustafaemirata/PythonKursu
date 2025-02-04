sayilar=[3,0,12,53,-1,45,77,84]
harfler=['a','g','ğ','z']
isimler=["mehmet","ali","ahmet","alperen","koray"]
sonuc=min(sayilar)
sonuc=max(harfler)

sonuc=min([len(isim) for isim in isimler])
sonuc=max([len(isim) for isim in isimler])

#Maximum karakterli ismi döndürür.
sonuc=max(isimler, key=lambda isim:len(isim))

urunler=[
    {"title":"samsung s23","price":70000},
    {"title": "samsung s24", "price": 80000},
    {"title": "samsung s25", "price": 90000},

]
#Minimum tutaarlı ürün bilgisini verdi.
sonuc=min(urunler, key=lambda urun: urun["price"])

#En pahalı ürünün title bilgisini verdi.
sonuc=max(urunler, key=lambda urun: urun["price"])["title"]

max=0
for urun in urunler:
    if(urun["price"]>max):
        max=urun["price"]
print(max)
print(sonuc)
