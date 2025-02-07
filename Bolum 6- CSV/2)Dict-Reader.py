import csv

with open("urunler.csv") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row["Category"] == "Telefon":
            print(row["ProductName"])
