# Topic 9 

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

cursor.execute("create DATABASE datarepresentation")

db.close()
cursor.close()