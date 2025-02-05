sayilar=[1,3,5,-3,74,82]

#Toplamın üzerine 15 ekler.
sonuc=sum(sayilar,15)

products=[
    {"title": "iphone 15","price":60000},
    {"title": "iphone 16", "price": 70000},
    {"title": "iphone 17", "price": 80000},
    {"title": "iphone 18", "price": 0}

]
toplamFiyat=sum([urun["price"] for urun in products])
urunAdedi=len([urun for urun in products if urun["price"]>0])
sonuc=toplamFiyat/urunAdedi

sonuc=round(5.3)
sonuc=round(5.3)
sonuc=round(5.8)

sonuc=round(1.321231,2)

print(sonuc)