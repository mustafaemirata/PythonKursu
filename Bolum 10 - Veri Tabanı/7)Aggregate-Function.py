import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

cursor=db.cursor()
#Toplam kayıt sayısı
#sql="SELECT COUNT(*) FROM products"

#Ortalama fiyatı getirir.
sql="SELECT AVG(price) FROM products"

#Toplam fiyatı getirir.
sql="SELECT sum(price) FROM products"

#Minimum fiyatı getirir.
sql="SELECT min(price) FROM products"

#Max price değerine sahip olan kayıdın tamamını getirme.
sql="SELECT name,price FROM products WHERE price=(SELECT MAX(price) FROM products)"

#Fiyatı azalacak şekilde yazdırır.
sql="SELECT name,price FROM products ORDER BY price DESC"

#sıralanmış listedeki ilk 2 kaydı getirir.
sql="SELECT name,price FROM products ORDER BY price DESC LIMIT 2"
cursor.execute(sql)
result=cursor.fetchall()
print(result)