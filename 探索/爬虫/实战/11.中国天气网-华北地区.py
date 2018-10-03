# encoding=utf-8

import json
import requests
from bs4 import BeautifulSoup
import bs4



saveObj = {}
# 解析页面
def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3567.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode("utf-8")
    soup = BeautifulSoup(text, 'lxml')
    # 全部地区
    nationBox = soup.find_all("div", class_="contentboxTab2")[0]

    # 保存 地区s
    partnamesList = nationBox.find("ul", class_="lq_contentboxTab2").stripped_strings
    for partname in partnamesList:
        saveObj[partname] = None
    
    # 某地区,多天
    partMulti = nationBox.find("div", class_="hanml")
    # 某地区,一天
    partSingle = partMulti.find("div", class_="conMidtab")
    partData = parse_part(partSingle)

    # 保存文件
    with open("./huabei.json", "w", encoding='utf8') as fp:
        fp.write( json.dumps( partData, ensure_ascii=False) )




# 解析地区
def parse_part(partSingle):
    result = {}
    for i,privince in enumerate(partSingle):
        
        # city: 某一个城市
        if type(privince) is not bs4.element.NavigableString:
            quxians = privince.find("table").find_all("tr")[2:]
            # 省份名
            provincename = quxians[0].find("td").find("a").string
            result[provincename] = None

            # 循环 区县列表
            cityData = {}
            cityname = None
            for k,quxian in enumerate(quxians):
                # 区县, tr, 一行;
                # 城市名
                cityname = quxian.find("a").string
                
                # 最高气温, 倒数第五个td
                toper = quxian.find_all("td")[-5:][0]
                # 最低气温, 倒数第二个td
                lasttd = quxian.find_all("td")[-2:][0]
                cityData[cityname] = {
                    "toper": toper.string,
                    "lower": lasttd.string
                }
                result[provincename] = cityData
                
    return result
    





# 主函数
def main():
    url = "http://www.weather.com.cn/textFC/hb.shtml"
    parse_page(url)

if __name__=='__main__':
    main()