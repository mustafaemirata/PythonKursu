#lamda
def kareAl(a):
    return a**2
sonuc=kareAl(5)
sonuc= (lambda a:a**2)(5)
kareAl= lambda a:a**2
sonuc2=kareAl(4)
print(sonuc2)
print(sonuc)

toplama=lambda a,b,c:a+b+c
sonuc3=toplama(3,4,9)

#Fonksiyon ile kullanımı
def myFunction(n):
    return lambda a:a*n
sonuc4= myFunction(2)(6)
print(sonuc4)

carpma2=myFunction(2)
sonuc5=carpma2(9)
print(sonuc5)