# coding=utf-8

from urllib import request,parse
import ssl
import json

# 定义请求头
header = {
    # 伪装浏览器
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    # 来源页面
    "Referer": "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC&district=%E4%B8%9C%E5%9F%8E%E5%8C%BA"
}

# 请求 url
url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&district=%E4%B8%9C%E5%9F%8E%E5%8C%BA&needAddtionalResult=false"

# 处理/忽略 https
context = ssl._create_unverified_context()

# 组装数据
data = parse.urlencode({
    "first": "true",
    "pn": 1,
    "kd": "python"
}).encode("utf-8")

# 定义请求对象
req = request.Request(url, headers=header, data=data, method="POST")

# 发送请求
resp = request.urlopen(req, context=context)

# 打印
result = resp.read().decode('utf8')
print(result)

# 尝试保存成文件
fileObj = open("./save.json", "w")
fileObj.write( json.dumps(result) )
fileObj.close()