# put all the individual SQL command python scripts into one
# use functions to store the scripts

import mysql.connector

#from config import con_host, con_user, con_password, con_database

class StudentDAO:
        
        host=""
        user=""
        password=""
        database=""
        connection=""
        cursor=""
        
        
        def __init__(self):
            # these should be read from a config file
            self.host="localhost",
            self.user="root",
            self.password="",
            self.database="datarepresentation"
        
        def getCursor(self):
              self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
              )
              self.cursor= self.connection.cursor()
              return self.cursor
        
        def closeAll(self):
              self.connection.close()
              self.cursor.close()

        def create(self, values):
              cursor = self.getCursor()
              sql="insert into student (name, age) values (%s,%s)"
              cursor.execute(sql, values)

              self.connection.commit()
              newid = cursor.lastrowid
              self.closeAll()
              return newid
        

        def getAll(self):
              #


        def findByID(self, id):
              
        
        def update(self, values):
              

        def delete(self, id):
              

studentDAO = StudentDAO()







sql="delete from student where id = %s"
values = (1,)

mycursor.execute(sql, values)

mydb.commit()
print("Delete Done")

mydb.close()
mycursor.close()