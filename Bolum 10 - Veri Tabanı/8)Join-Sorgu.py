import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

cursor=db.cursor()

sql="SELECT name, categoryid FROM products"
sql="SELECT name  FROM categories"
sql="SELECT * FROM products inner join categories on products.categoryId=categories.id"
cursor.execute(sql)

result=cursor.fetchall()
print(result)