# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import JsonLinesItemExporter



class ScrapyDashuzhaiPipeline(object):
    # 初始化函数
    def __init__(self):
        pass

    # 开始函数
    def open_spider(self, spider):
        self.fp = open("一梦到北大.txt", "a")
        self.fp.write("***** 一梦到北大 *****"+"\n\n\n")


    # 处理函数
    def process_item(self, item, spider):
        # 转换成对象(字典类型)
        item = dict(item)
        # 写入此章节的标题
        self.fp.write("\n\n-- "+item["title"]+" ------------------\n")

        # 遍历段落
        for text in item["texts"]:
            # 段首两个空格 + 段落内容 + 换行
            self.fp.write("   "+text+"\n")


    # 结束函数
    def close_spider(self, spider):
        self.fp.close()
