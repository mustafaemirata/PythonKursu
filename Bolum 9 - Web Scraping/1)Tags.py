from bs4 import BeautifulSoup
with open("index.html")as file:
    html=file.read()
obj=BeautifulSoup(html,"html.parser")
sonuc=obj
sonuc=type(obj)
sonuc=obj.prettify()

sonuc=obj.title
#bs4.elementtag
sonuc=type(obj.title)
#string kısmını yazdırır.
sonuc=obj.title.string

sonuc=obj.body
#h1 etiketini olduğu gibi yazdırır.
sonuc=obj.body.h1
#yazı değerini yazdırır.
sonuc=obj.body.h1.string

sonuc=obj.div
sonuc=obj.ul
print(sonuc)
