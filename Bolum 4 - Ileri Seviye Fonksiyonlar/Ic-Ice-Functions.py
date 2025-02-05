def fact(sayi):
    def inner_fact(sayi):
        if sayi<=1:
            return 1
        return sayi*inner_fact(sayi-1)
    return inner_fact(sayi)
sonuc=fact(5)