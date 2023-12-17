import mysql.connector


mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="datarepresentation"
)

mycursor = mydb.cursor()

sql="delete from student where id = %s"
values = (1,)

mycursor.execute(sql, values)

mydb.commit()
print("Delete Done")

mydb.close()
mycursor.close()