import mysql.connector


mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="data_rep"
)

mycursor = mydb.cursor()

sql="select * from student where id = %s"
values = (1,)

# print where id = 1
# for all print
# sql="select * from student"
# and remove the values in the cursor execute 

mycursor.execute(sql, values)
result = mycursor.fetchall()
for x in result:
    print(x)


mydb.close()
mycursor.close()