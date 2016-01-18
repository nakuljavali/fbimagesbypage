#!/usr/bin/python
import requests, json
global idList

__author__ = "Nakul Javali"
__email__ = "javali@usc.edu"

def main():
    print 'Generating html page...'

def getPicList():
    global idList
    idList = []
    r = requests.get('https://graph.facebook.com/v2.5/brainpickings.mariapopova/photos?type=uploaded&access_token=CAACEdEose0cBACjr2AMerEOX5ZA3X0k4TQ3xGZCPuEXxBBO5ZCNxHF9ekD2x1ob3uZAzt45bOobM3KjmKDxJzIdwtlPsKJybPYP4ptB93YuA96eN4uyUTc3PRcD6RhwhZAYnrB10AvgPbwrdvRfWsBYN75MOje4MQcCdaZAGUMdD6dWkwqNWkW1jXTD3tPbD0OlLIvy27YmnLGC6wuWiBi')
    json_data = json.loads(r.text)
    id_level = json_data['data']
    for ids in id_level:
        idList.append(ids['id'])

def getPics():
    file = open("pics.html", "wb")
    global idList
    file.write('<!DOCTYPE html>\n<html>\n<body>\n')
    for p in idList:
        file.write('<p><img src="https://graph.facebook.com/{0}/picture?type=normal"/></p>\n'.format(p))
    file.write('</body>\n</html>\n')

if __name__ == "__main__":
    main()
    getPicList()
    getPics()
