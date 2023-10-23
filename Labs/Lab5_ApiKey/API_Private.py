# Video Walk Through
# GitHub API

# https://docs.github.com/en/rest?apiVersion=2022-11-28
# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28

# get a repository's info
# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository


# When you set up a private repo and do a status check you get a 404 error if you do not have the keys
# this is to minimise the chances of it getting hacked

# I have set up a repo and I need my own personal access token

# url = "https://api.github.com/repos/VCurry20/aprivateone"

# tokens - Github - settings - developer settings
# Tokens - Classic - then there would be full access - what we used to use before to do pushes
# Fine grained one - we can limit access with this

# set up a fine grain token *** note this will expire ***
# set this only for the private repo I just set up

import requests
import json
from config import config as cfg

filename = "repo_private.json"

url = "https://api.github.com/repos/VCurry20/aprivateone"

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg

response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)