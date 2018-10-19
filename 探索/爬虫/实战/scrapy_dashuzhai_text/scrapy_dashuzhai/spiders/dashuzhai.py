# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
import json
import re
from scrapy_dashuzhai.items import ScrapyDashuzhaiItem


index = 1
class DashuzhaiSpider(scrapy.Spider):
    # name 和 allow_domains 是框架生成, 不用改;
    name = 'dashuzhai'
    allowed_domains = ['dashuzhai.com']

    # 访问的路径入口(例: <一梦到北大>这个小说内容的 第一页url)
    start_urls = ['http://www.dashuzhai.com/dushiyanqing/yimengdaobeida/54989.html']
    # 自定义的变量
    domain = "http://www.dashuzhai.com"
    
   
    def parse(self, response):
        global index  # 标注使用全局变量
        
        # 这是测试用的, 限制请求个数;
        # if index==3:
            # return False
        
        # 解析标题
        title = str(index)+". "+response.xpath("//div[@id='maincontent']/h1/text()")[0].get()
        # 解析段落对象
        paragraphs = response.xpath("//div[@id='content']/p")

        # 解析段落文字
        texts = []
        for paragraph in paragraphs:
            text = paragraph.xpath("./text()").getall()
            text = "".join(text).strip()
            # 过滤掉空格
            if text!="":
                texts.append(text)

        # 获取处理后的数据元;
        item = ScrapyDashuzhaiItem(title=title, texts=texts)
        # 把数据元送到 pipelines.py 文件中处理;
        yield item

        # 打印标题
        print("*"*30)
        print(title)
        print("*"*30)


        # 准备下一页面
        index = index+1
        next_url = response.xpath("//div[contains(@class,'prenext')]/span[last()]/a/@href").get()

        # 有url, 再次请求; 没有url,爬虫结束
        if not next_url:
            return False
        else:
            yield scrapy.Request(self.domain+next_url, callback=self.parse)
        
        
