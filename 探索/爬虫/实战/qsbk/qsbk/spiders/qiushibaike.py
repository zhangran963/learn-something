# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
import json
from qsbk.items import QsbkItem


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    baseDomain = "https://www.qiushibaike.com"

    def parse(self, response):
        # pass
        print("*"*30)

        duanziList = response.xpath("//div[@id='content-left']/div")

        for index,div in enumerate(duanziList):
            author = div.xpath(".//h2/text()").get().strip()
            text = div.xpath(".//div[@class='content']//text()").getall()
            # 过滤数据
            text = "".join(text).strip()

            item = QsbkItem(author=author, text=text)
            yield item
        
        # 判断下一页面
        nextUrl = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        
        if not nextUrl:
            return False
        else:
            yield scrapy.Request(self.baseDomain+nextUrl, callback=self.parse)