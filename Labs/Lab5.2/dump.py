from github import Github
import requests
from config import config as cfg

apikey = cfg["github"]

g = Github(apikey)

for repo in g.get_user().get_repos():
   print(repo.name)
   #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
   # print(dir(repo))

# make sure this replository exists, and that the path is correct
repo = g.get_repo("VCurry20/aprivateone")
print('this is print 1', repo.clone_url)

fileInfo = repo.get_contents("text.txt")
urlOfFile = fileInfo.download_url
print ('this is print 2', urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print ('this is print 3', contentOfFile)

newContents = contentOfFile + " more stuff 2 \n"
print ('this is print 4' , newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print ('this is print 5' , gitHubResponse)

#repo.update_file(fileInfo.path, "FileUpdated", newContents, fileInfo.sha, branch="developer")
#print('--> File test.txt (developer branch) updated.')