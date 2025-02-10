import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

cursor=db.cursor()
#cursor.execute("CREATE DATABASE exampleDb")
#cursor.execute("SHOW DATABASES")
#Bağlantıdaki database listelerini yazdırır.

cursor.execute("CREATE TABLE categories(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")




cursor.execute("SHOW TABLES")
for i in cursor:
    print(i)
