
* `pip3 install requests`安装 requests 库


### 基础
```py
import requests

# 请求百度
response = requests.get("https://www.baidu.com")

response.content  # 响应内容(未解码), bytes(字节流)数据
response.text  # 响应内容(自动解码, 可能乱码), unicode 格式的数据
response.content.decode("utf-8") # 手动解码

response.url     # 请求 url
response.encoding # 当前编码方式
```


### get请求
```py
import requests

# GET
params = {
    "wd": "中国"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
# 注: get请求发送 params; post 请求发送 data;
response = requests.get("http://www.baidu.com/s",params=params,headers=headers)

with open("baidu.html", "w", encoding="utf-8") as fp:
    fp.write(response.content.decode("utf-8"))
    print(response.url)
```

### post请求
```py
import requests


# POST
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
}
data = {
    "first": "true",
    "pn": "1",
    "kd": "python"
}
response = requests.post("https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false", data=data, headers=headers)

# 打印 json 数据
print(response.json())
# 保存 json 数据
with open("拉勾.html", "w", encoding="utf-8") as fp:
    fp.write(response.content.decode("utf-8"))
```