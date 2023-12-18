# Topic 4
# CSO data in multidiamential format = PxStat (can be looked at under different diamensions gender / location / age)

# CSO - https://data.cso.ie/#
# https://github.com/CSOIreland/PxStat/wiki/API-Cube-RESTful

# Choose dataset you want to look at
# - - scroll down to API data query and choose restful
# example 1 https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP001/JSON-stat/2.0/en
# title Preliminary Actual and Percentage Change in Population 2016 - 2022

# when you look at the API - try figure out the breakdown
# you need for loops for each diamension
# this one has 4 diamensions sex / county / census year and 2022 - actually importing it and looking at it is the easist way to figure it out
# in some instances you will not really have all the ones outlined  -break down in slides


import requests
import json

# Title: Preliminary Actual and Percentage Change in Population 2016 - 2022

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP001/JSON-stat/2.0/en"

def getAll():
    response = requests.get(url)
   # we could do checking for correct response code here
    return response.json()


if __name__=="__main__":
    with open("cso.json_all", "wt") as fp:
      print(json.dumps(getAll()), file=fp)




# get data set - this is data set FP001 - in this option we can pass this in and get the data

urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlend = "/JSON-stat/2.0/en"

def getAll2(dataset):
    url = urlBeginning + dataset + urlend  
    # have broken up and put together the url so that way we just need to code for the set and we can get the data
    response = requests.get(url)
   # we could do checking for correct response code here
    return response.json()


if __name__=="__main__":
    with open("cso.json_all2", "wt") as fp:
      print(json.dumps(getAll2("FP001")), file=fp)



# Example 3
# Alternative way to break up the code

def getAllAsFile(dataset):
   with open("cso.json_all3", "wt") as fp:
      print(json.dumps(getAll2(dataset)), file=fp)

def getAll3(dataset):
   url = urlBeginning + dataset + urlend  
   response = requests.get(url)
   return response.json()


def getFormattedAsFile(dataset):
   with open("cso.formatted.json", "wt") as fp:
      print(json.dumps(getAllFormatted(dataset)), file=fp) 


def getAllFormatted(dataset):
   data = getAll3(dataset)  # get all data
   ids = data["id"]
   values = data ["value"]
   dimensions = data["dimension"]
   sizes = data["size"]
   valuecount = 0  # count values
   result = {}
   #currentDict = result

# recursion is what would be needed to complete this without writing out all the code
   for dim0 in range(0, sizes[0]):
      currentId = ids[0]
      index = dimensions[currentId]["category"]["index"][dim0]
      label0 = dimensions[currentId]["category"]["label"][index]
      #print(currentId)
      #print (label0)
      result[label0]={}
      
      for dim1 in range(0, sizes[1]):
        currentId = ids[1]
        index = dimensions[currentId]["category"]["index"][dim1]
        label1 = dimensions[currentId]["category"]["label"][index]
        #print(currentId)
        #print ("\t",label1)
        result[label0][label1]={}

        for dim2 in range(0, sizes[2]):
            currentId = ids[2]
            index = dimensions[currentId]["category"]["index"][dim2]
            label2 = dimensions[currentId]["category"]["label"][index]
            #print(currentId)
            #print ("\t\t",label2)
            result[label0][label1][label2]={}
            

            for dim3 in range(0, sizes[3]):
                currentId = ids[3]
                index = dimensions[currentId]["category"]["index"][dim3]
                label3 = dimensions[currentId]["category"]["label"][index]
                #print(currentId)
                #print ("\t\t\t",label3, "", values[valuecount])
                result[label0][label1][label2][label3]= values[valuecount]
                valuecount+=1

   return result



   #for id in ids:  # test to see if this works
   #   print (id)


if __name__=="__main__":
    #getAllAsFile("FP001")
    getAllFormatted("FP001")
    getFormattedAsFile("FP001")
    