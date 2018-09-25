# encoding=utf-8

from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar("cookie-duan.txt")
cookiejar.load(ignore_discard=True)  # 已过期的 cookie 也打印出来
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)


# 打印某网址的 cookie 信息
resp = opener.open("http://httpbin.org/cookies")
for cookie in cookiejar:
    print(cookie)