import re

text="ABC 123 XYZ 456 @&% 300 1_2"
#3 sayı
#pattern=r"\d\d\d"

#en az bir basamaklı al
#pattern=r"\d+"

#0 olması durumunda da yazdırır. Boşlukları da yazdırır.
pattern=r"\d*"

# 3 basamaklıları bulur.
pattern=r"\d{3}"

# Minimum 3 maximum 5 basamaklıları yazdırır.
pattern=r"\d{3,5}"

#Max olmadan min 3 basamaklıları yazdırır.
pattern=r"\d{3,}"

#3 basamaklı olacak ortadaka karakter herhangi olsa da geri döndürür. 1.2, 1_9 ...
pattern=r"\d.\d"

#a'DAN z'YE ALMA.
pattern=r"[A,Z"

#matches=re.search(pattern,text)
matches=re.finditer(pattern,text)

#hepsini alır
matches=re.findall(pattern,text)



print(matches)

#Özel anlamı göz ardı etmek.
print(r"old\new")