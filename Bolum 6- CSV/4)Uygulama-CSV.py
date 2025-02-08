import csv

with open("onlinefoods.csv") as file:
    csv_reader=csv.reader(file)
    liste=list(csv_reader)
    #Toplam kayıt bulduk.
    print(len(liste)-1)

# yemek siparişi veren öğrenci sayısı listeleme
with open("onlinefoods.csv") as file:
    csv_reader=csv.DictReader(file)
    adet=len([user for user in csv_reader if user["Occupation"]=="Student"])
    print(adet)

#20-30 yaş arasında sipariş verenlerin konum listesini listeleme

with open("onlinefoods.csv") as file:
    csv_reader=csv.DictReader(file)
    users=(user for user in csv_reader if int(user["Age"]) > 20 and int(user["Age"])<30 )
    for i in users :
        print(i["latitude"],i["longitude"])