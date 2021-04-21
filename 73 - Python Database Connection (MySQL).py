# 73 - PYTHON DATABASE CONNECTION MySQL

import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='penk',passwd='SteveniX13')

mycursor = mydb.cursor()

mycursor.execute('show databases')

result = mycursor.fetchall()

for i in result:
    print(i)