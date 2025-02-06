def selamlama(fn):
    def inner(ad):
        print("Hoş Geldiniz.")
        fn(ad)
        print("Görüşmek üzere")
    return inner

@selamlama
def gunaydin(ad):
    print(f"Günaydın, benim adım {ad}")

@selamlama
def iyigunler(ad):
    print(f"İyi günler, benim adım {ad}")


gunaydin("Mahmut")
iyigunler("Ahmet")
