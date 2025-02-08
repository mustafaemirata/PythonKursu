import json
#with open("product.json") as file:
#    data=json.load(file)
#type=string olur.

data="""
{
  "id": 1,
  "title": "Mackbook Pro",
  "price": 90000,
  "rating":"4.5",
  "category": "Bilgisayar",
  "colors": ["Red", "Blue"]
}
"""
data=json.loads(data)
print(data)
print(data["title"])
print(data["colors"])
print(data["price"])

#serialize = encode
