liste = [1, 2, 3, 4]
print(len(liste))

# Hata: len() yalnızca listeler, stringler gibi koleksiyonlar için geçerlidir.
# sayi = 10
# print(len(sayi))  # TypeError verir

str_ = "Merhaba BTK Akademi"
print(len(str_))


class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    #description sağlar.

    def __del__(self):
        print("film silindi.")
    def __len__(self):
        return self.duration
    def __repr__(self):
        return f"{self.title} {self.director} tarafından {self.year} yılında yapıldı."


m = Movie("Film Adı", "Yönetmen", "Yayın Tarihi", 120)
print(m)
