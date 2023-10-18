# Data Representation
# Lab Topic 4
# Requests

# json() - turns a request into a dict and we can then analyise it


# Documentation
# https://requests.readthedocs.io/en/latest/
# https://github.com/psf/requests
# https://github.com/psf/requests/blob/main/src/requests/api.py


# Modules
# requests allows you to send HTTP requests to websites
# urllib.parse / urllib.parse.quote()- this is for encoding URLS / encodes spaces and special functions in a URL - allows you to turn a string into a URL Coded string
# urllib.parse.urlencode() - encodes parameters



# 1. test requests

import requests

url_test = "http://google.com"
response = requests.get(url_test)

# print (response.text)


# 1.1
# Check status code - - - - he wants both of these checks in the code 

# https://stackoverflow.com/questions/1140661/what-s-the-best-way-to-get-an-http-response-code-from-a-url
# https://www.geeksforgeeks.org/response-status_code-python-requests/
# https://nnamdi-okafor.medium.com/using-python-to-check-status-codes-ef0133fe16d4

#try:
  # r = requests.head("https://andrewbeatty1.pythonanywhere.com/books")
 #  print(r.status_code)

# prints the int of the status code. 

#except requests.ConnectionError:
#   print("failed to connect")


status = requests.get("https://andrewbeatty1.pythonanywhere.com/books")
# print(response.status_code)
  


# 2. Write the code to get the books from https://andrewbeatty1.pythonanywhere.com/books

url = "https://andrewbeatty1.pythonanywhere.com/books"
#response = requests.get(url)
# print (response.json())

# dump this and atl /ctrl/f to format



# 3. Convert into a function and call it from inside a if_name_=="_main_ :
# create functions for each API calls so we can seperate them and reuse them as needed

def getAllbooks():                         
   response = requests.get(url)
   # we could do checking for correct response code here
   return response.json()



# 4. Function fo finding by id and testing it

def getBookById (id):
   geturl = url + "/" + str(id)
   response = requests.get(geturl)
   return response.json() 
try:
    r = requests.head(url)
    print("The status code for the site is for ID check is:", r.status_code)
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")

# returns a dict object - note single quotes
# this is not returned as a json



# 5. Create and a book and test it

# https://www.datacamp.com/tutorial/making-http-requests-in-python
# you can test this by using Postman to check that posting is working on the site
# note that there is a more manual version outlined in the video

def createbook(book):
   #book = {
   #   'Author': "test",
   #   'Title' : "test title",
   #   'Price' : 123412
   #} # defines book

   response = requests.post(url, json=book)   # pass in the url you want to add to and the item you want to add / json=book adds as correct format
   return response.json()
   


# 6. Update Book

def updatebook(id, book):
   puturl = url + "/" +str(id)
   response = requests.put(puturl, json=book)
   return response.json()


# 7. Delete Book

# same as get book by id but here instead of get its delete

#def DeleteBookById (id):
#   geturl = url + "/" + str(id)
#   response = requests.delete(geturl)
#   return response.json()



# if / name / main
# this is to go at the end of all the methods  - it acts as a check that all is ok 

if __name__=="__main__":
   book = {
      'Author': "test test test",
      'Title' : "testing title",
      'Price' : 123412
   } # defines book 
   bookdiff = {
      'Author': "test test test",
      'Title' : "testing title",
      'Price' : 2222
   } # defines book 


   print ("These are all the books", getAllbooks())
   # print (getBookById(122))
   # print (createbook(book))
   # print (updatebook(324, bookdiff))
   # print (DeleteBookById(77))
  





########

# Notes

# add status checks - should checks give back more than just code -list of codes and return msg? if loop?
# 