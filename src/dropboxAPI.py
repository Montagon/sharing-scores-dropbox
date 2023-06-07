from urllib import request
from urllib.parse import urlencode
import requests, os
from base64 import b64encode
import dropbox

def refreshToken(appKey, appSecret, accessCode):
    body = {
        "code" : accessCode,
        "grant_type" : "authorization_code"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "Authorization": "Basic {}".format(
            b64encode(bytes(f"{appKey}:{appSecret}", "utf-8")).decode("ascii")
            )
    }
    url = "https://api.dropboxapi.com/oauth2/token"
    return requests.post(url, headers=headers, data=body)


def getRefreshToken(appKey, appSecret):
    print("Navigate to this URL and get ACCESS CODE:")
    print(f"https://www.dropbox.com/oauth2/authorize?client_id={appKey}&token_access_type=offline&response_type=code")
    print("Introduce ACCESS_CODE:")
    accessCode = input()
    return refreshToken(appKey, appSecret, accessCode).json()['refresh_token']

def getDropboxSession(appKey, appSecret, refreshToken):
    return dropbox.Dropbox(
        app_key = appKey,
        app_secret = appSecret,
        oauth2_refresh_token = refreshToken
    )

def generateLink(dbx, path):
    res = dbx.sharing_create_shared_link(path)
    return res.url

if __name__ == '__main__':
    appKey = os.environ['DROPBOX_APP_KEY']
    appSecret = os.environ['DROPBOX_APP_SECRET']
    print("Refresh token: ")
    print(getRefreshToken(appKey, appSecret))
