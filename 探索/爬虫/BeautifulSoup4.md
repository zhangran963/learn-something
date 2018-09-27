HTML/XML解析器, 基于 HTML DOM, 解析时遍历整个 DOM;

* 引入`from bs4 import BeautifulSoup`


### 用 bs 解析 html
* 解析库类型
    * "html.parser" python 自带解析器
    * "lxml" lxml 解析器
    * "html5lib" 最好的兼容性
示例:
```py
import requests
from bs4 import BeautifulSoup

html = '''
<div>
    siyecao
    <span>444</span>
</div>
'''
# 使用 lxml 解析器
bs = BeautifulSoup(html, "lxml")
```

### 获取所有某个元素
```py
...
soup = BeautifulSoup(html, "html5lib")
movieLis = soup.find_all("li")
```

### 获取 前n个标签
```py
soup = BeautifulSoup(html, "html5lib")
# 前三个li元素
movieLis = soup.find_all("li", limit=3)
# 第三个li元素
movieLi3 = soup.find_all("li", limit=3)[2]
```

### 获取指定 class 名的标签
```py
# class 是 python 中的关键字, 所以获取 类 要用 'class_' 代替;
movieLi = soup.find_all("li", class_='list-item')
# 或
movieLi = soup.find_all("li", attrs={ "class": "list-item" })
```

### 获取多个属性名的标签
```py
movieLi = soup.find_all("li", class_='list-item', id="27597216")
# 或
movieLi = soup.find_all("li", attrs={
    "class": "list-item",
    "id": "27597216"
})
```

### 获取属性值
```py
aElements = soup.find_all("a")
for aElement in aElements:
    # 直接用 元素['属性名'] 的方式读取属性值
    print( aElement["href"] )
    # 或
    print( aElement.attrs["href"] )
```

### 获取内容文本
```py
# 获取最后一个a元素, 读取文本
aElement = soup.find_all("a")[-1:][0]
print(aElement.string.strip())
```
