import json


class Product:
    def __init__(self,id,title,price):
        self.id=id
        self.tite=title
        self.price=price
# serialize
# p1 = Product(1, "Samsung S26", 87000)
# p2 = Product(2, "Samsung S27", 88000)
# p3 = Product(3, "Samsung S28", 89000)

# products = {
#     p1.id: p1.__dict__,
#     p2.id: p2.__dict__,
#     p3.id: p3.__dict__
# }

# print(p1.__dict__)

# import json
# with open("products.json", "w") as file:
#     json.dump(products, file)


#deserialize

with open("products.json") as file:
    produucts=json.load(file)
#tip: dict
print(type(produucts))
urunler=[]
for key,value in produucts.items():
    urunler.append(Product(key, value["tite"],value["price"]))
for p in urunler:
    print(p.tite)
#tip: list
print(type(urunler))