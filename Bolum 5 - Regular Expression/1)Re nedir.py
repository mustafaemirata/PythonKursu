import re
text="BTK Akademi Python Dersleri BTK"

#Aranacak karakter.
pattern="BTK"
match= re.search(pattern,text)
sonuc=match

sonuc=match.start()
sonuc=match.end()

#Tekrarlanmış karakterleri bulur.
match=re.findall(pattern,text)
sonuc=match

print(sonuc)