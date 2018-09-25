# encoding=utf-8

from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar("cookie-duan.txt")
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)


# # 1. 保存百度的 cookie
# resp = opener.open("http://www.baidu.com")
# cookiejar.save()


# 2.保存 (此会话结束时过期的)cookie 信息
resp = opener.open("http://httpbin.org/cookies/set?name=duanziqiong")
# cookiejar.save(ignore_discard=True)
for cookie in cookiejar: