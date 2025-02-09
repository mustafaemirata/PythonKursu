data ={
  "2": {
    "title": "Casper",
    "price": 80000
  },
  "3": {
    "title": "Casper",
    "price": 40000
  }
}
import json



with open("products.json") as file:
    products=json.load(file)
print(products["3"])

products.update({
    "1": {
        "title": "Monster",
        "price": 42312
    }
})
#Girilen ID değeri silinir.
products.pop("1")
with open("products.json","w",encoding="utf-8") as file:
    json.dump(products,file,ensure_ascii=False,indent=2)
