import requests

response=requests.post("https://jsonplaceholder.typicode.com/posts",data={

    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "Yeni gönderi açıklaması"

})

sonuc=response

#kaydedilmiş bilgiyi yazdırır. 100 kayıtlı id var. +1 olur id değeri 101 olur.
sonuc=response.text
sonuc=response.headers

sonuc=response.json()
print(sonuc)