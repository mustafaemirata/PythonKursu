sonuc=all([True,True,False])
sonuc=all([True,True,True])
sonuc2=any([True,True,True])
sonuc3=any([True,False,False])

#All'da tüm hepsi true olması lazım. Any'de bir tane olsa bile True döner.

print(sonuc)
print(sonuc2)
print(sonuc3)

sayilar=[1,3,5,7,6,52]
#Bütün sayılar 0'dan büyük mü?
sonuc=[bool(sayi) for sayi in sayilar]
#epsi çift mi?
sonuc=all([sayi%2==0 for sayi in sayilar])

#Hiç çift var mı?
sonuc=any([sayi%2==0 for sayi in sayilar])

users=["ahmet","çınar","ali"]
#Tüm kullanıcılar a harfiyle mi başlıyor?
sonuc=all([user[0]=='a'for user in users])

print(sonuc)