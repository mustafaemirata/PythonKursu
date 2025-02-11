import mysql.connector
import time
from cachetools import cached,TTLCache

db=mysql.connector.connect(
    host="localhost",
    user="emir",
    password="0634",
    database="shopdb"
)

# 1 saat tutulacak.
@cached(cache=TTLCache(maxsize=32,ttl=60))
def getProduct():
    cursor = db.cursor()
    sql = "SELECT p.name,c.name FROM products p inner join categories c on p.categoryId=c.id WHERE c.name='Bilgisayar'"
    cursor.execute(sql)
    print("from sql")
    return cursor.fetchall()

s=time.time()
print(getProduct())
print("Geçen zaman: ",time.time()-s)

#1.sinde süre alacak diğerrlerinde cacheden alacağı için süre geçmez.
s=time.time()
print(getProduct())
print("Geçen zaman: ",time.time()-s)

s=time.time()
print(getProduct())
print("Geçen zaman: ",time.time()-s)