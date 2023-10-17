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

#try:
  # r = requests.head("https://andrewbeatty1.pythonanywhere.com/books")
 #  print(r.status_code)

# prints the int of the status code. 

#except requests.ConnectionError:
#   print("failed to connect")


status = requests.get("https://andrewbeatty1.pythonanywhere.com/books")
print(response.status_code)




# 2. Write the code to get the books from https://andrewbeatty1.pythonanywhere.com/books

url = "https://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url)
#print (response.json())

# dump this and atl /ctrl/f to format





# 3. Convert into a function and call it from inside a if_name_=="_main_ :
# create functions for each API calls so we can seperate them and reuse them as needed

def readbooks():                         
   response = requests.get(url)
   # we could do checking for correct response code here
   return response.json()




# 4. Function fo finding by id and testing it

def getBookById (id):
   geturl = url + "/" + str(id)
   response = requests.get(geturl)
   return response.json()

# returns a string - note single quotes
# this would need to be changed to a dict 


# 5. Create and a book and test it

def createbook(book):

   response = requests.post(url, json=book)
   return response.json()
   
try:
    resp = requests.get(url)
    resp.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)  










# 7. Delete Book

# same as get book by id but here instead of get its delete

def DeleteBookById (id):
   geturl = url + "/" + str(id)
   response = requests.delete(geturl)
   return response.json()



# if / name / main
# this is to go at the end of all the methods  - it acts as
if __name__=="__main__":     
   # print (readbooks())
   print (getBookById(122))
   # print (DeleteBookById(77))