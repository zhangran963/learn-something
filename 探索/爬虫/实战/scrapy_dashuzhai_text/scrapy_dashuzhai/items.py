# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDashuzhaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 数据格式: 标题 + 段落数组
    title = scrapy.Field()
    texts = scrapy.Field()
