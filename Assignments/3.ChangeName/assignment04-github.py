# Assignment 04

# Write a program in python that will read a file from a repository
# The program should then replace all instances of the text "Andrew" with my name
# The program should then commit throse changes and push the fail back to the repository

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

response1 = requests.get(url)
print ("The status code is", response1.status_code)




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




if __name__=="__main__":
    ChangeName(file)