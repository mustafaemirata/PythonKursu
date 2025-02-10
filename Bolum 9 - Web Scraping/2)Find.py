from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:

    html=file.read()
obj=BeautifulSoup(html,"html.parser")

#Bulduğu ilk div elementini verir.
sonuc=obj.find("div")

#Tüm divleri verir.
sonuc=obj.find_all("div")

#Toplam div sayısı
sonuc=len(obj.find_all("div"))

#1.divdeki h2 elementi.
sonuc=obj.find_all("div")[1].h2

sonuc=obj.find_all("div")[1].ul.li

sonuc=obj.find_all("div")[1].ul.find_all("li")[2]

#Sadece Menü 6 yazısını aldırdık.
sonuc=obj.find_all("div")[1].ul.find_all("li")[2].string

#Tüm div elemanlarını yazdırdık.
for div in obj.find_all("div"):
    if div.h2.a!=None:
     print(div.h2.a.string.strip())
    else:
        print(div.h2.string.strip())
print(sonuc)

#Sayfadaki a etiketlileri bulup yazdırma.
for a in obj.find_all("a"):
    print(a)
