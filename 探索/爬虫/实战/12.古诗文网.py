# encoding=utf-8

import requests
from lxml import etree
import json
import re

# 网络下载文件
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3562.0 Safari/537.36"
}




def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    # 题目
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    # 朝代
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text)
    # 作者
    authors = re.findall(r'<div class="contson" .*?>(.*?)</div>', text, re.DOTALL)
    peoms = []

    # print(authors)
    for content in authors:
        x = re.sub(r'<.*>', "",content)
        peoms.append(x.strip())
        # print(x)
    print(peoms)






def main():
    url = "https://www.gushiwen.org/default_1.aspx"
    parse_page(url)


if __name__=='__main__':
    main()

