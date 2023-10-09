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

from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# check it works

# output to console to check / comment out once confirmed
# toprettyxml is a function of minidom where by it prints out a tidied version
# print (doc.toprettyxml()) 

# Store the xml in a file. complete the following / can also be commented out

# with open ("trainxml.xml", "w") as xmlfp:
#    doc.writexml(xmlfp)

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    trainCodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    trainCode = trainCodenode.firstChild.nodeValue.strip()
    print (trainCode)
    
    
#with open ("traincode.xml", "w") as traincode:
#        doc.writexml(traincode)
