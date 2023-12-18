from all_together import StudentDAO


#create
latestid = StudentDAO.create(('mark', 45))
# find by id
result = StudentDAO.findByID(latestid);
print ("test create and find by id")
print (result)

#update
StudentDAO.update(('Fred',21,latestid))
result = StudentDAO.findByID(latestid);
print("test update")
print (result)

# get all 
print("test get all")
allStudents = StudentDAO.getAll()
for student in allStudents:
  print(student)

# delete
StudentDAO.delete(latestid)

