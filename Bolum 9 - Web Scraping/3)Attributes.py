from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:

    html=file.read()
obj=BeautifulSoup(html,"html.parser")
sonuc=obj.div
#id değeri 1 olanı ekrana getir.
sonuc=obj.find(id="item1")
sonuc=obj.find(id="item2")
sonuc=obj.find(id="header")
#Class'ı item olan ilk elemanı ekrana getirir.
sonuc=obj.find(class_="item")

print(sonuc)