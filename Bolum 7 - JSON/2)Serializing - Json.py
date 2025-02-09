import json
product={
  "id": 2,
  "title": "Mackbook Pro",
  "price": 90000,
  "rating":"4.5",
  "category": "Bilgisayar",
  "colors": ["Red", "Blue"]
}
print(product)
# dict gösterilir.
print(type(product))

#sonuc=json.dumps(product)
#print(sonuc)
# FARK! Bu str veri oldu. Dict değil.
#print(type(sonuc))
#print(product["title"])

#Türkçe karakter ve yazım şekli parametreye eklendi.
with open("product.json","w",encoding="utf-8") as file:
    json.dump(product,file,ensure_ascii=False,indent=2)