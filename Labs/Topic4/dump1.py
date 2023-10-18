
## code dump

import requests

url = "https://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url)

try:
    r = requests.head("https://stackoverflow.com")
    #print(r.status_code)
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")



try:
    resp = requests.get(url)
    resp.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)  





# 5. Create and a book and test it

# https://www.datacamp.com/tutorial/making-http-requests-in-python

def createbook(book):
   response = requests.post(url, json=book)
   return response.json()
   
try:
    resp = requests.get(url)
    resp.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)  



# alternative version for create

def createbook(book):
   book = {
      'Author': "test",
      'Title' : "test title",
      'Price' : 123412
   }
   headers ={ "content-type": "application / json"}
   response = requests.post(url, data=json.dumps(book), headers=headers)
   return response.json()
   