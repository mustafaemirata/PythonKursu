import json

products = {
    "1": {
        "title": "Casper",
        "price": 80000
    },
    "2": {
        "title": "Casper",
        "price": 40000
    }
}

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)

db = {
    "users": {
        "mustafaemirata": {
            "firstname": "mustafaemir",
            "lastname": "ata"
        },
        "mehmeteymenata": {
            "firstname": "mehmeteymen",
            "lastname": "ata"
        }
    },
    "product": products
}

with open("db.json", "w", encoding="utf-8") as file:
    json.dump(db, file, ensure_ascii=False, indent=2)

print(db["users"]["mustafaemirata"])

db["product"].update({
    "3": {
        "title": "Samsung J7",
        "price": 2800
    }
})

with open("db.json", "w", encoding="utf-8") as file:
    json.dump(db, file, ensure_ascii=False, indent=2)
