### request
引入`from urllib import request`
```
f = request.open("http://www.baidu.com")
# 开头得是http://, https还不会处理;
f.status  # 200
f.reason  # OK

for key,value in f.getheaders():
    print("%s:::%s" % (key,value))
    # 按键值对的形式打印出header信息, 类似浏览器显示的;
```