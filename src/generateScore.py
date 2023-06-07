from os import listdir, environ
import os
import re
from unittest import result
import dropboxAPI
import configHelpers
import scoreHelpers


appKey = os.getenv('DROPBOX_APP_KEY')
appSecret = os.getenv('DROPBOX_APP_SECRET')
refreshToken = os.getenv('DROPBOX_REFRESH_TOKEN')

if appKey is None or appKey == "":
    print("ERROR: The 'DROPBOX_APP_KEY' must be set")
    exit()
if appSecret is None or appSecret == "":
    print("ERROR: The 'DROPBOX_APP_SECRET' must be set")
    exit()
if refreshToken is None or refreshToken == "":
    print("ERROR: The 'DROPBOX_REFRESH_TOKEN' must be set")
    exit()

config = configHelpers.readConfig()
dbx = dropboxAPI.getDropboxSession(appKey, appSecret, refreshToken)

print("Introduce directory:")
scorePath = input()
path = scorePath

pathDropbox = re.sub(".*Dropbox", "", path).replace(os.path.sep,'/')
scoreName = path.split(os.path.sep)[-1]

elements = configHelpers.getSearchElements(config)
content = [x.lower() for x in listdir(path)]

final = []
for e in elements:
    el = list(filter(lambda v: re.match(f".*{e}.*", v), content))
    if(len(el) > 0):
        if (el[0] != None):
            path = pathDropbox + "/" + el[0]
            uri = dropboxAPI.generateLink(dbx, path)
            final.append(uri)
        else:
            final.append("")
    else:
        final.append("")

elementsWithURL = configHelpers.getElementsWithURL(config, final)
print("Introduce video URL:")
videoURL = input()

result = scoreHelpers.generateScore(scoreName, videoURL, elementsWithURL)
scoreHelpers.writeScore(scorePath, scoreName, result)