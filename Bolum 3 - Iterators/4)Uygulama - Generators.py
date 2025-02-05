# 1'den sonsuza kare alma.

#def sayi_uret():
# #sayi=0
# while True:
#      yield sayi**2
 #       sayi+=1
#generator=sayi_uret()
#print(next(generator))


#for i in generator:
#   print(i)

# 2.Fibonacci
def fib_list(max):
    sayilar = []
    a, b = 0, 1

    while len(sayilar) <= max:
        sayilar.append(b)
        a, b = b, a + b

    return sayilar

print(fib_list(25440))
