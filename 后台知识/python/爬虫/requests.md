* 安装`pip3 requests`
* 引入`import requests`

简单试用
```
r = requests.get("http://www.baidu.com")
r.text  # 内容(字符串形式)
r.reason  # OK
r.status_code  # 状态码
r.url  # 这个请求的url
r.encoding  # 编码形式
r.json()  # 以json形式解码返回的内容(类型错误时报错)
json.loads(r.text)  # 通用json解析数据
```
请求头
```

```

键值对
```
myparam = {
    "name": "四叶草"
}
r = requests.get("https://www.baidu.com", params = myparam)
r.url
# https://www.baidu.com/?name=%E5%9B%9B%E5%8F%B6%E8%8D%89
```
