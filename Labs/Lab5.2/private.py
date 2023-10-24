# Get Private Data from Github
# Write and push info to your repository
# Change repository

import requests
import json

from github import Github

from config import config as cfg

filename = "repo_private.json"

url = "https://api.github.com/repos/VCurry20/aprivateone"

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["github"]

response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)