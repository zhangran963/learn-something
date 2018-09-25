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

# POST
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
