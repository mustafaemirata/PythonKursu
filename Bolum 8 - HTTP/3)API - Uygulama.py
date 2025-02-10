import requests

url=" http://api.weatherapi.com/v1/current.json"
key="4ccd47ddea3c498c80e90820251002"

konum=input("konum: ")

response=requests.get(url,params={
    "key":key,
    "q":konum,
    #türkçe dil eklendi.
    "lang":"tr"
})

sonuc=response.json()
sehir=sonuc["location"]["name"]
havadurumu=sonuc["current"]["temp_c"]

text=sonuc["current"]["condition"]["text"]

print(sonuc)
print(havadurumu)
print(text)

print(f"{sehir} şu anda {havadurumu} deree ve {text}")