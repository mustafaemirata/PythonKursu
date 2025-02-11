import time
import threading

def calculate_square(numbers):
    print("sayıların kareleri hesaplanıyor.")
    for i in numbers:
        time.sleep(0.3)
        print("kare",i*i)
def calculate_cube(numbers):
    for i in numbers:
        time.sleep(0.3)

        print("sayının kübü: ",i*i*i)
sayilar=[1,2,4,6,23,5]
t=time.time()

calculate_square(sayilar)
calculate_cube(sayilar)

#işlem parçacığı
t1=threading.Thread(target=calculate_square,args=(sayilar,))
t2=threading.Thread(target=calculate_cube,args=(sayilar,))

t1.start()
t2.start()

t1.join()
t2.join()

print("işlem tamamlandı: ",time.time()-t)