# _*_ coding:utf-8 _*_

import requests
from lxml import etree
import json


def getHtmlNodes(url, xpathStr):
    html = requests.get(url)
    root = etree.HTML(html.text)
    htmlNodes = root.xpath(xpathStr)
    return htmlNodes


# 获取 M 站的真实链接
def getMissevanUrl(url):
    xpath = '//*[@id="info"]/div[1]/p[2]/iframe'
    if "music.163.com" in url:
        xpath = '//*[@id="info"]/div[1]/p[3]/iframe'
    elif 'https://www.leasmr.com/tr/ppomo' in url:
        xpath = '//*[@id="info"]/div[1]/p[4]/iframe'


    htmlNodes = getHtmlNodes(url, xpath)
    oldUrl = htmlNodes[0].get("src")
    return oldUrl
    # print(oldUrl)
    

# 获取这个网站的音色封面 详情页面的URL https://www.leasmr.com/tr/page/1
# {
#     "name": "小芒果阿",
#     "url": "https://www.leasmr.com/tr/as913",
#     "articleUrl": "https://www.missevan.com/albumiframe/238496?autoplay=false&playlist=false"
# }

# 写入文件
def writeToFile(data, fileName):
    json_str = json.dumps(data, indent=4)

    with open(fileName, 'w') as json_file:
        json_file.write(json_str)

def getLeasmrTrDetailUrls():
    leasmrTrDetailObj = []
    for i in range(2):
        page = str(i + 1)
        urlStr = "https://www.leasmr.com/tr/page/" + page
        htmlNodes = getHtmlNodes(urlStr, "//article")
        for node in htmlNodes:
            obj = {}
            obj["url"] = node[0][0].get("href")
            obj["name"] = node[1][0][0].text
            if "live" in obj["url"]:
                continue
            elif "https://www.leasmr.com/tr/as905" in obj["url"]:
                continue
            else:
                leasmrTrDetailObj.append(obj)
    return leasmrTrDetailObj

arr = getLeasmrTrDetailUrls()
for obj in arr:
    obj["articleUrl"] = getMissevanUrl(obj["url"])

writeToFile(arr, 'newAllData.json')

