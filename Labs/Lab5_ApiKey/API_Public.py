# Video Walk Through 
# GitHub API

# https://docs.github.com/en/rest?apiVersion=2022-11-28
# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28

# get a repository's info
# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository

import requests
import json


# in both of these examples we are getting information from public pages

# overview URL 
url_pub = "https://api.github.com/repos/andrewbeattycourseware/datarepresentation"

filename1 = "repo_public.json"

response1 = requests.get(url_pub)
print ("The status code is", response1.status_code)

repoJSON1 = response1.json()
# print (response.json())


with  open(filename1, 'w') as fp:
    repoJSON1 = response1.json()
    json.dump(repoJSON1, fp, indent=4)



# contents URL
url_contents = "https://api.github.com/repos/VCurry20/data-representation-coursework"

#"https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code"

filename2 = "repo_contents.json"

content_response = requests.get(url_contents)
print ("This is the contents page response", content_response.status_code)

contentRepo = content_response.json
# print (content_response.json())

with  open(filename2, 'w') as fp:
    repocontentsJSON = content_response.json()
    json.dump(repocontentsJSON, fp, indent=4)