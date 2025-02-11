import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

cursor=db.cursor()

#sql="SELECT *FROM products WHERE Id>1"
#sql="SELECT *FROM products WHERE name='Samsung S26'"

#Hem iphone hem samsung 2 kayıt getirir.
#sql="SELECT * FROM products WHERE name='Samsung S25' OR price=97000"

#içinde Iphone geçen kayıtları alma
#sql="SELECT * FROM products WHERE name LIKE '%Iphone%'"

#Iphone ile başlayan kayıtları alma
#sql="SELECT * FROM products WHERE name LIKE 'Iphone%'"

#Iphone ile biten kayıtları alma
#sql="SELECT * FROM products WHERE name LIKE '%Iphone'"

#İçinde samsung olan veya açıklamasında iyi olan kayıtları birleştirerek getirir.
sql="SELECT * FROM products WHERE name LIKE '%Samsung%' OR description LIKE '%iyi%'"



#id'si 1 olan dinamik kayıt oluşturduk.
cursor.execute(sql)


def getProductById(id):
    # yer tutucu
    sql = "SELECT * FROM products WHERE id=%s"
    params = (id,)
    result = cursor.fetchall()
    print(result)
getProductById(1)