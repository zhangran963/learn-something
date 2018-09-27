# encoding=utf-8

import requests
from lxml import etree
import json

# 网络下载文件
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3562.0 Safari/537.36"
}
response = requests.get("https://movie.douban.com/cinema/nowplaying/beijing/", headers=headers)
htmlElement = etree.HTML(response.content.decode("utf-8"))


# # 本地读取文件
# parser = etree.HTMLParser(encoding='utf-8')
# htmlElement = etree.parse("./douban.html", parser=parser)


movieLis = htmlElement.xpath("//div[@id='nowplaying']//ul[@class='lists']/li")
movies = []
for movieLi in movieLis:
    movie = {}

    lis = movieLi.xpath(".//li[position()<4]")
    
    movie['poster'] = lis[0].xpath("./a/img/@src")[0]
    movie['name'] = lis[1].xpath("./a/text()")[0].strip()
    movie['star'] = (lis[2].xpath("./span[last()]/text()")[0].strip())
    
    # print(movie)
    movies.append(movie)

    with open("douban-nowplaying-movies.json", "w", encoding='utf-8') as fp:
        fp.write(json.dumps(movies))
