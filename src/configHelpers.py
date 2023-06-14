import json
from collections import namedtuple
from json import JSONEncoder

class Instrument:
    def __init__(self, name, restrictLevel, publishName):
        self.name = name
        self.restrictLevel = restrictLevel
        self.publishName = publishName

class InstrumentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def instrumentDecoder(instrumentDict):
    return namedtuple('X', instrumentDict.keys())(*instrumentDict.values())

def readConfig(toClass = True):
    with open("application.conf", 'r') as configFile:
        if toClass:
            return json.load(configFile, object_hook=instrumentDecoder)
        else:
            return json.load(configFile)

def getSearchElements(config):
    res = []
    for row in config:
        res.append(row.name)
    return res

def getElementsWithURL(config, urls):
    for i in range(0, len(urls)):
        config[i]["url"] = urls[i]
    return config

if __name__ == '__main__':
    config = readConfig(True)
    print(getSearchElements(config))
