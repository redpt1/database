import pymysql

def connectdb():
    db = pymysql.connect(host='39.102.140.167', user='root', password="whatafuck123924", database='my_db',port=3306)
    return db


