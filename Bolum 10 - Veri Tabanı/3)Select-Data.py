import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

cursor=db.cursor()

#sql="SELECT * FROM products"

#daha performanslı
sql="SELECT Id,name  FROM products"

cursor.execute(sql)
#tüm sonuçları listeleme
#products=cursor.fetchall()

#Sadece ilk kaydı filtreleyerek getirir.
products=cursor.fetchone()
print(products)
#id ve ürün ismi
#for p in products:
#    print(p[0],p[1])