# Trains

# Write a program that prints data for all trains in Ireland to the console. ( Store to a CSV File)
# Web Address : http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML

# Then as an exercise only store trains that have a train code that starts with D

# Tip: For datasets of this size you can get all the data first and then perform analysis / deletions later.


# Links
# https://docs.python.org/3/library/xml.dom.minidom.html


# Process

# Go to the URL / check it works / View format of Data
# Create a python program that reads the XML from the URL and prints it out using minidom.
# Check it works

import requests   # makes a request to a webpage
import csv        # lists data as a csv / csv format
import pandas as pd
import numpy as np
import re 

from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# check it works

# output to console to check / comment out once confirmed
# toprettyxml is a function of minidom where by it prints out a tidied version
# print (doc.toprettyxml()) 

# Store the xml in a file. complete the following / can also be commented out

with open ("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)


# print out the train codes - this prints to console
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    trainCodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    trainCode = trainCodenode.firstChild.nodeValue.strip()
    print (trainCode)
    

# print out the longitudes - this prints to console  
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    TrainLongitudenode = objTrainPositionsNode.getElementsByTagName("TrainLongitude").item(0)
    Longitudecode = TrainLongitudenode.firstChild.nodeValue.strip()
    print (Longitudecode)


# print Train codes to CSV file
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row

with open('traincodes.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        trainCodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        trainCode = trainCodenode.firstChild.nodeValue.strip()
     #print (trainCode)

        dataList = []
        dataList.append(trainCode)
        train_writer.writerow(dataList)

# print longitudes to CSV file

with open('Longitudes.csv', mode='w', newline='') as Longitude_file:
    Longitude_writer = csv.writer(Longitude_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        TrainLongitudenode = objTrainPositionsNode.getElementsByTagName("TrainLongitude").item(0)
        Longitudecode = TrainLongitudenode.firstChild.nodeValue.strip()
    #print (Longitudecode)
        
        dataList = []
        dataList.append(Longitudecode)
        Longitude_writer.writerow(dataList)


# print all details of trains using their tags
# for loop used

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]


with open('train_all.csv', mode='w', newline='') as train_fileall:
    train_writerall = csv.writer(train_fileall, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
    
        dataList2 = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList2.append(datanode.firstChild.nodeValue.strip())

        train_writerall.writerow(dataList2)



# filter all items - TrainCode - D
#####
# 
check = 'D'


with open('traincodes_D.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        trainCodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        trainCode = trainCodenode.firstChild.nodeValue.strip()
     #print (trainCode)

        dataList_D = []
        dataList.append(trainCode)
        train_writer.writerow(dataList_D)

res = [idx for idx in dataList_D if idx[0].lower() == check.lower()]

print res(dataList_D)
