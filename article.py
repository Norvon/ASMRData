# _*_ coding:utf-8 _*_

import requests
from lxml import etree
import json

def getHtmlNodes(url, xpathStr):
    html = requests.get(url)
    root = etree.HTML(html.text)
    htmlNodes = root.xpath(xpathStr)
    return htmlNodes


# 获取声音列表
def getSoundList(url):
    soundList = []
    htmlNodes = getHtmlNodes(url, "//div[@class='magic-box-inner']")
    for node in htmlNodes:
        soundIma = node[0][0]
        soundA = node[2][0][0]

        obj = {}
        soundImageUrl = soundIma.get("src")
        soundName = soundA.text
        soundUrl = soundA.get("href")

        obj["soundImageUrl"] = "https:" + soundImageUrl
        obj["soundName"] = soundName
        obj["soundUrl"] = "https://www.missevan.com" + soundUrl
        soundList.append(obj)
    return soundList


def getData(url):
    album = {}
    album["albumImageUrl"] = getHtmlNodes(
        url, '//*[@id="channel_zone"]/span/img')[0].get("src")

    album["albumName"] = getHtmlNodes(
        url, '//*[@id="channel_zone"]/span/img')[0].get("alt")

    album["albumUserName"] = getHtmlNodes(
        url, '//*[@id="explore_right"]/div[1]/div[2]/div/a')[0].text

    album["soundList"] = getSoundList(url)
    return album

# 写入文件
def writeToFile(data, fileName):
    json_str = json.dumps(data, indent=4)

    with open(fileName, 'w') as json_file:
        json_file.write(json_str)


def main(url): 
    # requestUrl = "https://www.missevan.com/albuminfo/238496"
    data = getData(url)
    fileName = "./soundData/" + data["albumName"] + '.json'
    writeToFile(data, fileName)
