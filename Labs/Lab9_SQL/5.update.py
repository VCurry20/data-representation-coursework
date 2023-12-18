import mysql.connector


mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="data_rep"
)

mycursor = mydb.cursor()

sql="update student set name= %s, age=%s where id = %s"
values = ("Joe", 22, 1)

mycursor.execute(sql, values)

mydb.commit()
print("Update Done")

mydb.close()
mycursor.close()