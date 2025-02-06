def douuble (fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)

    return inner
@douuble
def merhaba(isim):
    print("Merhaba", isim)

@douuble
def selam(isim):
    print("Selam",isim)
@douuble
def iyiGunler():
    return "İyi Günler"

merhaba("Murat")
selam("Murata")
print(iyiGunler())
