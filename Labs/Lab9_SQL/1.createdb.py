# Topic 9 

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

cursor.execute("create DATABASE data_rep")

db.close()
cursor.close()