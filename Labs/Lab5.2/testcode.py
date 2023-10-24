# to use this install package
# pip install PyGithub


from github import Github
import requests
from config import config as cfg

import numpy as np
import pandas as pd


apikey = cfg["github"]

g = Github(apikey)

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))



# make sure this repository exists, and that the path is correct
repo = g.get_repo("VCurry20/aprivateone") 
print("this is the last bit that works", repo.clone_url)

# https://medium.com/plumbersofdatascience/import-and-export-files-to-and-from-github-via-api-626efd7dd859

datatest = pd.read_csv("employees.csv")

with open('VCurry20/aprivateone/text.csv', 'x') as file:
    data = datatest

repo.create_file('/VCurry20/aprivateone/text.csv', 'upload csv', datatest)


#fileInfo = repo.get_contents("test.txt")
#urlOfFile = fileInfo.download_url
#print (urlOfFile)

#response = requests.get(urlOfFile)
#contentOfFile = response.text
#print (contentOfFile)

#newContents = contentOfFile + " more stuff 2 \n"
#print (newContents)

#gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
#print (gitHubResponse)