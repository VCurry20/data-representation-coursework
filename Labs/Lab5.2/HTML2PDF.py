# Topic 5
# Lab 1

# API Keys
# Websites
# https://html2pdf.app/
# https://docs.github.com/en/rest/guides

# hide key
# https://www.reddit.com/r/git/comments/xn0j88/how_to_ignore_config_files_without_adding_them_to/
# https://stackoverflow.com/questions/62939781/adding-files-to-gitignore-in-visual-studio-code


import requests
import urllib.parse

from config import config as cfg

targetUrl = "https://en.wikipedia.org/wiki/Main_Page"
apiKey = cfg["html"]


# HTMLtoPDF Docs - https://html2pdf.app/documentation/
apiUrl = "https://api.html2pdf.app/v1/generate"


params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiUrl +"?" + parsedparams

response = requests.get(requestUrl)
print (response.status_code)

result =response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)
