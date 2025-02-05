def counter(max):
    sayi=1
    sayilar=[]

    while sayi<=max:
        yield sayi
        sayi+=1

    return sayilar
generator=counter(20)
print(dir(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print(next(generator))
print("------------------")
# 1'den 19'a kadar yazdırma.
liste=[i for i in range(1,20)]
print(liste)
