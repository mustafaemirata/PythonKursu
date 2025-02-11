import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

cursor=db.cursor()

sql="INSERT INTO products (name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"

#value=("Iphone 16",70000,"3.png","İ iyi telefon")
values=[
    ("Samsung 17",30000,"4.png","iyi telefon"),
    ("Samsung 18",40000,"5.png","iyi telefon"),
    ("Samsung 18",57000,"6.png","iyi telefon")


]
#tekse execute çoksa aşağıdaki.
cursor.executemany(sql,values)

#veritabanına gönderme işlemi.
try:
    db.commit()
    print(cursor.rowcount," kayıt edildi.")
    print(f"Son eklenen kayıdın id değeri:{cursor.lastrowid}")
except mysql.connector.Error as err:
    print("Hata: ",err)
finally:
    cursor.close()
    db.close()
    print("Bağlantı kapandı.")