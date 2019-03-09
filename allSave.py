import article

data = [{
        "name": "小芒果阿",
        "url": "https://www.leasmr.com/tr/as913",
        "articleUrl": "https://www.missevan.com/albuminfo/238496"
        },
        {
        "name": "MTkoala-",
        "url": "https://www.leasmr.com/tr/mtkoala",
        "articleUrl": "https://www.missevan.com/albuminfo/150397"
        },
        {
        "name": "小狐岁三w-",
        "url": "https://www.leasmr.com/tr/as909",
        "articleUrl": "https://www.missevan.com/albuminfo/150919"
        },
        {
        "name": "工口小菊花-",
        "url": "https://www.leasmr.com/tr/as908",
        "articleUrl": "https://www.missevan.com/albuminfo/151686"
        },
        {
        "name": "双马尾馨儿（睡前故事/日常 & ASMR）",
        "url": "https://www.leasmr.com/tr/as910",
        "articleUrl": "https://music.163.com/outchain/player?type=4&id=7225014&auto=0&height=430"
        },
        {
        "name": "音频- 保持关注即可",
        "url": "https://www.leasmr.com/tr/ppomo",
        "articleUrl": "https://www.missevan.com/albuminfo/147573"
        },
        {
        "name": "Tomatomato",
        "url": "https://www.leasmr.com/tr/tomatomato",
        "articleUrl": "https://www.missevan.com/albuminfo/151268"
        },
        {
        "name": "清软喵",
        "url": "https://www.leasmr.com/tr/as915",
        "articleUrl": "https://www.missevan.com/albuminfo/238499"
        },
        {
        "name": "南征-",
        "url": "https://www.leasmr.com/tr/as904",
        "articleUrl": "https://www.missevan.com/albuminfo/186233"
        },
        {
        "name": "诱情ASMR",
        "url": "https://www.leasmr.com/tr/as912",
        "articleUrl": "https://www.missevan.com/albuminfo/238498"
        },
        {
        "name": "轩子巨2兔",
        "url": "https://www.leasmr.com/tr/xuanzi",
        "articleUrl": "https://music.163.com/outchain/player?type=4&id=340642067&auto=1&height=430"
        },
        {
        "name": "隔壁班的喵会长",
        "url": "https://www.leasmr.com/tr/as916",
        "articleUrl": "https://www.missevan.com/albuminfo/262695"
        },
        {
        "name": "小芸豆儿",
        "url": "https://www.leasmr.com/tr/as911",
        "articleUrl": "https://www.missevan.com/albuminfo/238497"
        },
        {
        "name": "妖卿子-",
        "url": "https://www.leasmr.com/tr/as907",
        "articleUrl": "https://www.missevan.com/albuminfo/151860"
        },
        {
        "name": "合集第一期（M站）",
        "url": "https://www.leasmr.com/tr/as906",
        "articleUrl": "https://www.missevan.com/albuminfo/147579"
        },
        {
        "name": "Rappeler",
        "url": "https://www.leasmr.com/tr/rappeler",
        "articleUrl": "https://www.missevan.com/albuminfo/152731"
        }
        ]



if __name__ == "__main__":
    for item in data:
        url = item["articleUrl"]
        if ("www.missevan.com" in url):
            article.main(url)
    pass
