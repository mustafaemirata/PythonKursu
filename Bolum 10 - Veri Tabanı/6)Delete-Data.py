import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

cursor=db.cursor()
sql="DELETE FROM products WHERE id=1"
cursor.execute(sql)

try:
    db.commit()
    print(f"{cursor.rowcount} tane kayıt silindi.")
except mysql.connector.Error as err:
    print(err)
finally:
    db.close()
    cursor.close()
#Diğer dosyadaki fonksiyon yapısının aynısı olduğundan silme fonksiyonunu eklemedim.