urlopen()
* request.urlopen( url, data?)

* 返回 http.client.HTTPResponse 对象;
    * 通过 .read( size? ) 读取值;
        * .read().decode("utf8") 把 读取完的数据 解码;
    * .readline() 读取1行;
    * .readlines() 读取多行;
    * .info() 读取头部信息;
    * .getcode() 获取状态码;


urlretrieve
* 把服务器文件下载到本地;
* request.urlretrieve("http://www.baidu.com", 保存的文件名)


urlencode
* 给发送的字段编码;
```py
from urllib import parse

param = {'name': '张三'}
a = parse.urlencode(param)
# name=%E5%BC%A0%E4%B8%89
```
```py
url = "http://www.baidu.com/s"
param = {'wd': '刘德华'}
url = url+'?'+parse.urlencode(param)
```

parse_qs
* 给字段解码
```py
b = parse.parse_qs( "http://www.baidu.com/s?wd=%E5%88%98%E5%BE%B7%E5%8D%8E" )
print(b)   
# {'http://www.baidu.com/s?wd': ['刘德华']}
```

urlparse
* 解析 url 中每个组成部分
```py
url = "http://www.baidu.com/s?wd=python?username=abc#1"
result = parse.urlparse(url)
# result.scheme 协议
# result.netloc 域名
# result.path 路径
# result.query 字段
# result.fragment 锚点值
# 特 result.params (这个可忽略)
```
urlsplit
* 同 urlparse, 解析 url 中每个组成部分



Request 类
```py
# 定义请求对象
req = request.Request(url, headers=header, data=data, method="POST")
```

ProxyHandler 处理器(代理)