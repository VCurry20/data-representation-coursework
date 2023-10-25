from github import Github
import requests
import json
from config import config as cfg

import numpy as np
import pandas as pd

url = "https://api.github.com/repos/VCurry20/data-representation-coursework"

file = "employees.csv"
name1 = "Andrew"
name2 = "Veronica"

#url_contents = "https://github.com/VCurry20/data-representation-coursework/tree/main/Assignments"
g = Github()
#repo = g.get_repo("VCurry20/aprivateone")

response = requests.get(url)
print ("Site Status Code:", response.status_code)
#print (response.json())


# make sure this replository exists, and that the path is correct
repo = g.get_repo("VCurry20/data-representation-coursework")
print('Confirmation of Repository:', repo.clone_url)

file_location = g.get_repo("VCurry20/data-representation-coursework").get_contents("/Assignments")
#fileInfo = file_location.get_contents("txt.txt")
#urlOfFile = file_location.download_url
#print ('this is print 2', file_location)
#print ("this is the url", urlOfFile)
    

def ChangeName (data):
# reading the CSV file 
    text = open(data, "r") 
#join() method combines all contents of  
# csvfile.csv and formed as a string 
    text = ''.join([i for i in text])  
# search and replace the contents 
    text = text.replace(name1, name2)  
# output.csv is the output file opened in write mode 
    x = open("output.csv","w") 
# all the replaced text is written in the output.csv file 
    x.writelines(text)
    print("Names have now been amended")
    x.close()





#if __name__=="__main__":
    #ChangeName(file)