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
    htmlNodes = getHtmlNodes(url, '//*[@id="info"]/div[1]/p[2]')
    # for node in htmlNodes:
    node = htmlNodes[0]
    oldUrl = node[0].get("src")
    print(oldUrl)
    # if "www.missevan.com" in oldUrl:
    #     arr = oldUrl.split("?")
    #     if len(arr) == 2:
    #         missevanUrl = arr[0].replace("iframe", "info")
    #         print(missevanUrl)
    


# 获取这个网站的音色封面 详情页面的URL https://www.leasmr.com/tr/page/1
def getLeasmrTrDetailUrls():
    leasmrTrDetailUrls = []
    for i in range(2):
        page = str(i + 1)
        urlStr = "https://www.leasmr.com/tr/page/" + page
        htmlNodes = getHtmlNodes(urlStr, "//article")
        for node in htmlNodes:
            url = node[0][0].get("href")
            # print(url)
            if "live" in url:
                continue
            else:
                leasmrTrDetailUrls.append(url)
    return leasmrTrDetailUrls


for leasmrTrDetailUrl in getLeasmrTrDetailUrls():
    getMissevanUrl(leasmrTrDetailUrl)

