# Assignment 3

# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO
# & stores it into a file called "cso.json"

# Exchequer Account (Historical Series) 
# CSO Data Code: FIQ02
# API URL
# https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en



import requests   
import json


# have broken up and put together the url so that way we just need to code for the set and we can get the data
urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlend = "/JSON-stat/2.0/en"
dataset = "FIQ02"
url = urlBeginning + dataset + urlend 


# get dataset function - all data from site - as json
def getAll(dataset):
    response = requests.get(url)
    # we could do checking for correct response code here
    return response.json()

# check the status code of the site - this will return to the console
try:
    r = requests.head(url)
    print("The status code for the site is for ID check is:", r.status_code)
except requests.ConnectionError:
        print("failed to connect")


# run code and print to json file
if __name__=="__main__":
    with open("cso.json", "wt") as fp:
      print(json.dumps(getAll(dataset)), file=fp)