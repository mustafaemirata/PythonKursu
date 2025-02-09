data=[
  {
  "id": 1,
  "title": "Macbook Pro",
  "price": 80000
  },
   {
  "id": 2,
  "title": "Macbook Air",
  "price": 70000
  }
]
import json

product=  {
  "id": 3,
  "title": "Samsung S23",
  "price": 40000
  }
with open("products.json") as fie:
    products=json.load(fie)

for p in products:
    if[p["title"]=="Samsung S23"]:
        p["title"]="Casper"

products.remove(products[1])

#products.append(product)

with open("products.json","w",encoding="utf-8") as file:
    json.dump(products,file,ensure_ascii=False,indent=2)