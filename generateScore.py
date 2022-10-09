from os import listdir, environ
import re
from unittest import result
import dropboxAPI
import configHelpers
import scoreHelpers

appKey = environ['DROPBOX_APP_KEY']
appSecret = environ['DROPBOX_APP_SECRET']
refreshToken = environ['DROPBOX_REFRESH_TOKEN']

config = configHelpers.readConfig()
dbx = dropboxAPI.getDropboxSession(appKey, appSecret, refreshToken)

print("Introduce directory:")
scorePath = input()
path = scorePath

pathDropbox = re.sub(".*Dropbox", "", path).replace('\\','/')
scoreName = path.split("\\")[-1]

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