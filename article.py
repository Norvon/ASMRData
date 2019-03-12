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
    htmlNodes = getHtmlNodes(url, '//*[@id="playlist"]/div[1]/ul/li')

    for node in htmlNodes:
        soundA = node
        obj = {}
        # soundImageUrl = soundIma.get("src")
        soundName = soundA[1].text
        soundUrl = soundA.get("data-soundurl64")
        soundSinger = soundA[2].text

        # obj["soundImageUrl"] = "https:" + soundImageUrl
        obj["sound_name"] = soundName
        obj["sound_url"] = "https://www.missevan.com" + soundUrl
        obj["sound_singer"] = soundSinger
        soundList.append(obj)
    return soundList


def getData(url):
    album = {}
    album["album_image_url"] = getHtmlNodes(
        url, '//*[@id="player"]/div[1]/img')[0].get("src")

    album["album_name"] = getHtmlNodes(
        url, '//*[@id="player"]/div[2]/div[1]/marquee/a')[0].text

    # album["albumUserName"] = getHtmlNodes(
    #     url, '//*[@id="explore_right"]/div[1]/div[2]/div/a')[0].text

    album["sound_list"] = getSoundList(url)
    return album

# 写入文件
def writeToFile(data, fileName):
    json_str = json.dumps(data, indent=4)

    with open(fileName, 'w') as json_file:
        json_file.write(json_str)


def main(url): 
    data = getData(url)
    fileName = "./soundData/" + data["album_name"] + '.json'
    writeToFile(data, fileName)
    
# 南征
# main("https://www.missevan.com/albumiframe/186233?autoplay=false&playlist=true&shadow=true")
