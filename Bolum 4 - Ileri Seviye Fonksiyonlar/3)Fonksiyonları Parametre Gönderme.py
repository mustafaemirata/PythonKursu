def filter(fn, liste):
    result=[]
    for item in liste:
        if fn(item):
            result.append(item)
    return result
def is_even(num):
    return num%2==0
def is_positive(num):
    return num>0
sayilar=[1,2,3,5,7,8,9,22,11,-32]
sonuc=filter(is_even,sayilar)
sonuc=filter(is_positive,sayilar)


print(sonuc)