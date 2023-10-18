# topic 4 / Lecture 2
# Reading Data from datagov.ie
# https://data.gov.ie/


# https://opendata.valoff.ie/api/

# how many sq foot of hair salons in Wicklow
# office

# filter this site for wicklow and office 
# Query URL - use this for your functions

# https://api.valoff.ie/api/Property/GetProperties


import requests
import json
from inspect import Parameter
import urllib.parse

# Data as json
url = "https://opendata.tailte.ie/api/Property/GetProperties"


# Same URL just to allow me to showing testing - this is also available in CSV format
url2 = "https://opendata.tailte.ie/api/Property/GetProperties?Fields=LocalAuthority%2CCategory%2CLevel%2CAreaPerFloor%2CNavTotal%2CCarPark%2CPropertyNumber%2CUse%2CFloorUse%2CAddress%2CPublicationDate&LocalAuthority=WICKLOW%20COUNTY%20COUNCIL&CategorySelected=OFFICE&Format=csv&Download=false"

#### print the site to a file to ensure all works first

# 1. test the site works first - print to console

def getAll():                         
   response = requests.get(url2)
   # we could do checking for correct response code here
   return response.json()

# print to test - create json files as there is a lot of data



# 2. set parameters
# take them from the url and we will then be able to amend the data
# break down the URL - you can see an original one above and here the parameters taken from it
# 2c = , - you can check this by looking at the printed version

parameterasDict = {
    "Download":"false",
    "Format":"json",
    "CategorySelected":"OFFICE",
    "LocalAuthority":"WICKLOW COUNTY COUNCIL", # change this to get mayo CC for example - in caps
    "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG%,Use,FloorUse,Address,PublicationDate"
}


def getAnalysis(): 
   parameters = urllib.parse.urlencode(parameterasDict)
   #print(parameters) 
   fullurl = url + "?" + parameters
   
   response = requests.get(fullurl)
   return response.json()



if __name__=="__main__":
   #print (getAnalysis())
   # this first print will not be very clear and will not print to json - leaving as an example
   # atl shift F will format it // note the single quotes
   with open("valoff.json", "wt") as fp:
      print(getAll(), file=fp)
    # this will open proper json file
    #formatted alt shift f
   with open("valoff2.json", "wt") as fp:
      print(json.dumps(getAll()), file=fp)
   with open("valoff_analysis.json", "wt") as fp:
      print(json.dumps(getAnalysis()), file=fp)
    

