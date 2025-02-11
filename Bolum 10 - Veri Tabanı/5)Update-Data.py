import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

cursor=db.cursor()


def updateProduct(id,name,price):
    sql = "UPDATE products SET name=%s,price=%s WHERE id=%s"

    #params sıralaması önemli!!
    params=(name,price,id)
    cursor.execute(sql,params)
    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()
updateProduct(2,"Samsung A54 - Updated",23000)
