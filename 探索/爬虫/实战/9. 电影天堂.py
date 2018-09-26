# encoding=utf-8

import requests
from lxml import etree

domain = "http://dytt8.net"
url = "http://dytt8.net/html/gndy/dyzz/list_23_1.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


# 获取某页面中的详情页 url
def getDetailUrls(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    return map(lambda url: domain+url, detail_urls)


# 获取单个电影信息
def parseDetailPage(url):
    movie = {}

    response = requests.get(url, headers=headers)
    text = response.content.decode("gbk")
    html = etree.HTML(text)

    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    movie["cover"] = imgs[0]
    movie["screenshot"] = imgs[1]


    def parseInfo(info,rule):
        return info.replace(rule,"").strip()

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = parseInfo(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parseInfo(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parseInfo(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎主　　演"):
            info = parseInfo(info, "◎主　　演")
            actors = []
            for x in range(index+1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith("0"):
                    break
                actors.append(actor)
        elif info.startswith("◎简　　介"):
            info = parseInfo(info, "◎简　　介")
            for x in range(index+1, len(infos)):
                profile = infos[x].strip()
                movie["profile"] = profile

        
    downloadUrl = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['downloadUrl'] = downloadUrl

    return movie




def spider():
    baseUrl = "http://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    # 循环页数
    for x in range(1,2):
        url = baseUrl.format(x)
        detailUrls = getDetailUrls(url)
        
        # 循环每页中的电影 url
        for detailUrl in detailUrls:
            movie = parseDetailPage(detailUrl)
            movies.append(movie)
            print(movie)

    print(movies) 


if __name__=='__main__':
    spider()

# urls = getDetailUrls(url)
# print(urls)