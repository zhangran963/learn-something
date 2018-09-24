# coding=utf-8

from urllib import request,parse
import ssl
import json

url = "http://httpbin.org/ip"

# 创建代理服务器
handler = request.ProxyHandler({
    "http": "118.190.95.35:9001"
    # "http": "61.135.217.7:80"
})
opener = request.build_opener(handler)
# 打开
resp = opener.open(url)

print(resp.read().decode("utf-8"))