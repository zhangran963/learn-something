### 根节点
* 以`//`开始


### 子孙节点
* `//div/img`: 获取 div元素下的 img 子标签;
* `//div//img`: 获取 div元素下的 img 子孙标签;


### 根据索引获取元素
* `//body/div[1]`: 获取 body的 第一个div子元素(注: 第一个元素已1开头);
* `//body/div[last()]`: 获取 body的 最后的div子元素;
* `//body//form/input[position()<3]`: 获取 form 的前两个 input 子元素;


### 根据属性获取元素
* `//book[@price]`: 选择所有有 price 属性的元素;
* `//div[@class='s_position_list']`: 获取 `<div class='s_position_list'></div>` 这样的元素;
* `//div[contains(@class, 'f1')]`: 获取 `<div class='f f1 f2'></div>` 这样的包含`f1`的元素;
* `//div[@class='job' and @id='job-box']`: 获取`<div class='job' id='job-box'></div>` 这样的元素;
    * `!=`: `price!=9.8`
    * `<`: `price<9.8`, 另有`<=` `>` `>=`等
    * `or`: `price>9.8 or price=9`


### 属性值
```py
# src是属性值的字符串
src = htmlElement.xpath("//div[2]//img/@src").get()
```


### 元素值
```py
name = htmlElement.xpath("//div[2]//span/text()")[0]

### 方式1, 获取多个相隔的字符串
# text 是字符串组成的数组
texts = htmlElement.xpath("//div[2]//span/text()").getall()
# 合并数组字符串并去掉前后的空格
content = "".join(texts).strip()


### 方式2, 获取单个字符串(第一个字符串)
# text 是字符串
text = htmlElement.xpath("//div[2]//span/text()").get()
# 去掉前后的空格
text = text.strip()
```


### 当前元素的子元素
```py
# 获取当前元素的后代元素用 "." 起始, 例如".//"或"./"
tr.xpath(".//a/@href")
```