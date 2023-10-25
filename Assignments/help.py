# Assignment 04

# Write a program in python that will read a file from a repository
# The program should then replace all instances of the text "Andrew" with my name
# The program should then commit throse changes and push the fail back to the repository

from github import Github
import requests
import json
#from config import config as cfg

import numpy as np
import pandas as pd

url = "https://api.github.com/repos/VCurry20/data-representation-coursework"
data = "employees.csv"

for repo in g.get_user().get_repos():
   print("Confirm name of Repository", repo.name)


fileInfo = repo.get_contents("text.txt")
urlOfFile = fileInfo.download_url
print ('this is print 2', urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print ('this is print 3', contentOfFile)




# reading the CSV file 
text = open(data, "r") 
  
#join() method combines all contents of  
# csvfile.csv and formed as a string 
text = ''.join([i for i in text])  
  
# search and replace the contents 
text = text.replace("Andrew", "Veronica")  

  
# output.csv is the output file opened in write mode 
x = open("output.csv","w") 
  
# all the replaced text is written in the output.csv file 
x.writelines(text) 
x.close()



#def replace_char(string):
#    new_str = ""
#    for c in string:
#        if c ==  "Andrew":
#            new_str += "Veronica"
#       else:
#            new_str += c
#    return new_str


#print(replace_char(datatest))