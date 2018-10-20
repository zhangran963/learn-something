# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
import json
import re
from scrapy_dashuzhai.items import ScrapyDashuzhaiItem


index = 1
class DashuzhaiSpider(scrapy.Spider):
    name = 'dashuzhai'
    allowed_domains = ['dashuzhai.com']
    start_urls = ['http://www.dashuzhai.com/dushiyanqing/yimengdaobeida/54989.html']
    domain = "http://www.dashuzhai.com"
    
   
    def parse(self, response):
        global index
        
        # if index==5:
        #     return False
        
        title = str(index)+". "+response.xpath("//div[@id='maincontent']/h1/text()")[0].get()
        paragraphs = response.xpath("//div[@id='content']/p")


        texts = []
        for paragraph in paragraphs:
            text = paragraph.xpath("./text()").getall()
            text = "".join(text).strip()
            if text!="":
                texts.append(text)

        # 保存
        item = ScrapyDashuzhaiItem(title=title, texts=texts)
        yield item

        # 打印
        print("*"*30)
        print(title)
        print("*"*30)


        # 下一页面
        index = index+1
        next_url = response.xpath("//div[contains(@class,'prenext')]/span[last()]/a/@href").get()

        if not next_url:
            return False
        else:
            yield scrapy.Request(self.domain+next_url, callback=self.parse)
        
        

