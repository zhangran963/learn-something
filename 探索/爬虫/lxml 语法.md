### 读取网络文件
引入lxml并使用
```py
from lxml import etree

text = """
    <div>
        <input type='text'  />
    </div>
"""

htmlElement = etree.HTML(text)


htmlElement.xpath("//input[@class])
# 或
etree.tostring(htmlElement)
```

使用etree
* `etree.tostring(源, encoding='utf-8')` 把源内容转换成 bytes 类型;
* `etree.tostring(源, encoding='utf-8').decode('utf-8')`: 把源内容转成字符串;



### 读取本地文件
使用 etree.parse()
```py
from lxml import etree

html = etree.parse("./baidu.html")
result

```