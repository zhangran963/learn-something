# encoding=utf-8

import requests
from lxml import etree
import json
import re
import csv
import pymongo
import threading
import time
import random
from urllib import request
import os
from queue import Queue


# 添加这个后, 就解决了 ssl 问题#
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# 生产者:获取到图片路径
class Producer(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3562.0 Safari/537.36"
    }

    def __init__(self, pageQueue, imgQueue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.pageQueue = pageQueue
        self.imgQueue = imgQueue
    
    def run(self):
        while True:
            if self.pageQueue.empty():
                break
            url = self.pageQueue.get()
            self.parsePage(url)

    def parsePage(self, url):
        url = "http://www.doutula.com/photo/list?page="

        for index in range(10,101):
            urll = url+str(index)
            response = requests.get(urll, headers=self.headers)
            text = response.text
            
            html = etree.HTML(text)
            imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")

            for img in imgs:
                imgUrl = img.get("data-original")  # 远程url
                imgFormat = os.path.splitext(imgUrl)[1]  # 格式
                imgName = img.get("alt")  # 图片名称

                # 保存 (网络图片路径, 本地图片路径.格式)
                self.imgQueue.put((imgUrl, "%s%s" %(imgName, imgFormat)))

# 消费者:下载图片
class Consumer(threading.Thread):
    def __init__(self, pageQueue, imgQueue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.pageQueue = pageQueue
        self.imgQueue = imgQueue

    def run(self):
        while True:
            if self.imgQueue.empty() and self.pageQueue.empty():
                break
            imgUrl, imgName = self.imgQueue.get()   # 解构
            request.urlretrieve(imgUrl, "images/%s" %(imgName))


# 创建队列和多个线程(生成者 & 消费者)
def main():
    pageQueue = Queue(100)
    imgQueue = Queue(1000)

    for index in range(1, 101):
        url = "http://www.doutula.com/photo/list?page=%d" %index
        pageQueue.put(url)
    
    # 创建生产者多进程
    for x in range(5):
        t = Producer(pageQueue, imgQueue)
        t.start()

    # 创建消费者多进程
    for x in range(5):
        t = Consumer(pageQueue, imgQueue)
        t.start()      
    


if __name__=='__main__':
    main()