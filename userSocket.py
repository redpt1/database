import socket
import pymysql
import sys

#serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 信息传输socket
seInfoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #验证信息端口

db = pymysql.connect(host='39.102.140.167', user='root', password="whatafuck123924", database='my_db',port=3306)
cursor = db.cursor()





