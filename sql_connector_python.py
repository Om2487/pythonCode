import mysql.connector

conn=mysql.connector.connect(host='localhost',database='osk',user='root',password='@om.OSK759014')
cursor=conn.cursor()
print(conn.is_conncted())
