# coding=utf-8

from urllib import request,parse
from http.cookiejar import CookieJar
import ssl
import json

headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6"
}
# 创建 opener
def getOpener():
    # 创建 cookieJar 对象
    cookiejar = CookieJar()
    # 使用 cookieJar 创建
    handler = request.HTTPCookieProcessor(cookiejar)

    opener = request.build_opener(handler)
    return opener


# 登录
def login(opener):
    # 登录 url
    url_login = "http://www.renren.com/PLogin.do" 
    data = {
        "email": "1490515876@qq.com",
        "password": "963963"
    }
    req = request.Request(url_login, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)


# 获取内容页
def getPage(opener):
    # 获取登录后页面时, 不能新建 opener , 因为之前的 opener 已经包含了登录的 cookie;
    # 我的主页地址
    url_ran = "http://www.renren.com/968147767/profile"
    req = request.Request(url_ran, headers=headers)
    resp = opener.open(req)

    return resp


# 开始
opener = getOpener()
login(opener)
resp = getPage(opener)
# 保存
with open("renre.html", "w", encoding="utf-8") as fp:
    fp.write(resp.read().decode("utf-8"))