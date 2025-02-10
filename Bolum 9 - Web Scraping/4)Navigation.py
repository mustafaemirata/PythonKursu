from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:

    html=file.read()
obj=BeautifulSoup(html,"html.parser")

sonuc=obj.body.div.contents[3]

#for i in obj.body.div.children:
#    print(i)

#Alt elemanların da alt elemanlarını verir.
for i in obj.body.div.descendants:
    print(i)
print("------------")

#Üst elemanına ulaştırmaktadır.
sonuc=obj.body.h2.parent

sonuc=obj.body.div.next_sibling.next_sibling
print(sonuc)

