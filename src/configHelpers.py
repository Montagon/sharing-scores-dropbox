import json

def readConfig():
    with open("application.conf", 'r') as configFile:
        return json.load(configFile)

def getSearchElements(config):
    res = []
    for row in config:
        res.append(row['name'])
    return res

def getElementsWithURL(config, urls):
    for i in range(0, len(urls)):
        config[i]["url"] = urls[i]
    return config

if __name__ == '__main__':
    config = readConfig()
    print(getSearchElements(config))
