# _*_ coding:utf-8 _*_

import requests
from lxml import etree
import json
import copy

for idex in range(7):  
    index = str(idex + 1)
    urlStr = "https://www.asmrv.com/gw/page/" + index

    html = requests.get(urlStr)
    root = etree.HTML(html.text)
    # 获取所有 article 节点
    excerpts = root.xpath('//article')

    # 存储数据
    data = []
    # 遍历 excerpts
    for excerpt in excerpts:

        #正确的节点包括图片、描述和footer 
        if (len(excerpt) == 3):
            d = {}
            d["dataSrc"] = excerpt[0][0].get("data-src")
            d["href"] = excerpt[1][0].get("href")
            d["text"] = excerpt[1][0].text
            data.append(d)
    # print(json.dumps(data))

    arr = copy.deepcopy(data)
    # 详情页面节点
    for i in range(len(arr)):
        obj = arr[i]
        detailHtml = requests.get(obj["href"])
        detailRoot = etree.HTML(detailHtml.text)
        # 详情页面的播放器
        detailArticles = detailRoot.xpath('//article')
        for item in detailArticles:
            # print(item[0].get("src"))
            dic = data[i]
            dic["url"] = item[0].get("src")

    # print(data)
    # 格式化数据为json字符串
    json_str = json.dumps(data, indent = 4)
    # print(json_str)

    fileName = "./video/"+ index + '.json'
    with open(fileName, 'w') as json_file:
        json_file.write(json_str)
