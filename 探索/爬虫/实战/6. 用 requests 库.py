import requests


# params = {
#     "wd": "中国"
# }
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
}

# # GET
# response = requests.get("http://www.baidu.com/s",params=params,headers=headers)

# # POST
# data = {
#     "first": "true",
#     "pn": "1",
#     "kd": "python"
# }
# response = requests.post("http://httpbin.org/ip")

# print(response.text)

# 使用代理
response = requests.get("http://httpbin.org/ip", proxies={
    "https": "123.207.30.131:80"
})

print(response.content.decode("utf-8"))
