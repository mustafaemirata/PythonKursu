import csv

#with open("urunler.csv") as file:
#    print(file.read())  # Dosyanın tamamını okur ve imleç sona gider

with open("urunler.csv") as ile:  # Tekrar aç
    csv_reader = csv.reader(ile)  # Doğru değişken kullan
    #Liste elemanı haline getirir.
  #  liste=list(csv_reader)
  #  print(liste[1])  # CSV içeriğini liste olarak yazdır

    #Kolon numarasına göre alır.
    next(csv_reader)
    for i in  csv_reader:
        print(i[0])