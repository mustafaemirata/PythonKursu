sayilar=[1,2,3,4,5]
iterator=iter(sayilar)

# Hata vermesini önledik.
while True:
     try:
         sayi=next(iterator)
         print(sayi)
     except StopIteration:
         break