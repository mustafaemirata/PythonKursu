# 1- 100 arasında 12'ye tam bölünen list-comp ile yaz.
sonuc=[i for i in range(1,101) if i%3==0 if i%4==0]
print(sonuc)

# Verilen test içerisindeki rakamları içeren bir liste oluşturma.
#text="Hello World" => [1,2,3,4,5]

text="Hello 12345 Wor97ld"
sonuc=[i for i in text if i.isdigit()]
print(sonuc)
# Sıcaklık Listesi
sicakliklar=[20,15,0,-5,-2]
sonuc=[i if i>=4 else "Buzlanma Tehlikesi"for i in sicakliklar]
print(sonuc)

for x in range(3):
    for y in range(3):
        sonuc.append((x,y))
# list-comp ile yazımı:
sonuc=[(x,y,z)  for x in range(3) for y in range(3) for z in range(3)]
print(sonuc)