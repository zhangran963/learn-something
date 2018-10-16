# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json




# # 1.手动保存数据成 json 文件;
# class QsbkPipeline(object):
#     def __init__(self):
#         pass


#     def open_spider(self, spider):
#         self.fp = open("duanzi.json", "w", encoding="utf-8")


#     def process_item(self, item, spider):
#         JItem = json.dumps(dict(item), ensure_ascii=False)
#         # 写入并换行
#         self.fp.write(JItem + "\n")
 

#     def close_spider(self, spider):
#         self.fp.close()



# # 2. 已字典形式保存 item 数据
# # 先把数据收集成 列表, 然后一起写入 json文件, 可能会占内存
# from scrapy.exporters import JsonItemExporter

# class QsbkPipeline(object):
#     def __init__(self):
#         pass

#     def open_spider(self, spider):
#         self.fp = open("duanzi.json", "wb")
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding="utf-8")
#         self.exporter.start_exporting()

#     def process_item(self, item, spider):
#         self.exporter.export_item(item)

#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()


# # 3. 以单项的形式保存 item 数据(同第一个方法效果相同)
# # 一条一条地写入 json文件
from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        pass

    def open_spider(self, spider):
        self.fp = open("duanzi.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding="utf-8")

    def process_item(self, item, spider):
        self.exporter.export_item(item)

    def close_spider(self, spider):
        self.fp.close()