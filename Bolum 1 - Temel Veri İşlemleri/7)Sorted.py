sayilar=[1,87,3,23,94,75]
sonuc=sorted(sayilar)
print(sonuc)

users=[
    {"username": "mustafaemirata", "posts": ["post1", "post2"],"email":"info@abc.com", "phone":"1234"},
    {"username": "emir", "posts": ["post1", "post2","post3"], "email": "info@dfg.com"},
    {"username": "ata", "posts": ["post1"], "email": "info@zzv.com"},

]
sonuc=sorted(users, key=len)
#Alfabetik sıra
sonuc=sorted(users, key=lambda user: user["username"])

#Post sayısı en az olandan en çok olana sıralama
sonuc=sorted(users, key=lambda user: user["posts"])
#En çoktan en aza
sonuc=sorted(users, key=lambda user: user["posts"],reverse=True)

#En azdan en çoka post paylaşan usernameler.
sonuc=list(map(lambda user: user["username"],sorted(users, key=lambda user:len(user["posts"]))))

kurslar=[
    {"title": "python","count":100000},
    {"title": "web geliştirme", "count": 200000},
    {"title": "python", "count": 50000},

]
#Katılan sayısı en azdan en çoka doğru sıraladık. Reverse olduğunda en çoktan en aza listeyi ters çevirir.
sonuc=sorted(kurslar,key=lambda kurs:kurs["count"],reverse=True)
#En çoktan en az katılan kursların isimlerini yazdırma.
sonuc=list(map(lambda kurs:kurs["title"],sorted(kurslar,key=lambda kurs:kurs["count"],reverse=True)))
print(sonuc)

