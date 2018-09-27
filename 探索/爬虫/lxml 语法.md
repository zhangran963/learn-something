### 解析字符串
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
使用 etree.parse(源, parser=解析器) 解析, 默认解析器是 XML 解析器;
```py
from lxml import etree

# 指定 html 解析器, 并使用
parser = etree.HTMLParser(encoding='utf-8')
htmlElement = etree.parse("./baidu.html", parser=parser)
```