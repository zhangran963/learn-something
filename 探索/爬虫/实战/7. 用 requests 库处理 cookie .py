# encoding=utf-8

import requests


url_login = "http://www.renren.com/PLogin.do"
data = {
    "email": "1490515876@qq.com",
    "password": "963963"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}

# 创建 session
session = requests.session()
# 登录
session.post(url_login, data=data, headers=headers)

# 获取主页
url_ran = "http://www.renren.com/968147767/profile"
response = session.get(url_ran)

with open("renren.html", "w", encoding="utf-8") as fp:
    fp.write(response.text)