sayilar=[1,2,3,5,-4,-5]

def negatifSayilar(x):
    if x<0:
        return True
    else:
        return False

sonuc=list(filter(lambda x: x<0,sayilar))
sonuc=list(filter(lambda x: x%2==1,sayilar))

isimler=["çınar","ali","ada","yiğit","sena"]
filterResult=list(filter(lambda  x: x[0]=='a',isimler))
sonuc=list(map(lambda x: x.upper(),filterResult))

users=[
    {"username":"mustafaemirata","posts":["post1","post2"]},
    {"username": "mehmet", "posts": ["post1"]},
    {"username": "murat", "posts": []},
    {"username": "emir", "posts": ["post1", "post2","post3","post4"]},
]
sonuc=list(filter(lambda u:len(u["posts"])>3,users))
sonuc=list(map(lambda u: u["username"],list(filter(lambda u:len(u["posts"])>3,users))))
print(sonuc)