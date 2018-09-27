根节点
* 以`//`开始


子&子孙节点
* `//div/img`: 获取 div元素下的 img 子标签;
* `//div//img`: 获取 div元素下的 img 子孙标签;


第n个元素
* `//body/div[1]`: 获取 body的 第一个div子元素(注: 第一个元素已1开头);
* `//body/div[last()]`: 获取 body的 最后的div子元素;
* `//body//form/input[position()<3]`: 获取 form 的前两个 input 子元素;


属性
* `//book[@price]`: 选择所有有 price 属性的元素;
* `//div[@class='s_position_list']`: 获取 `<div class='s_position_list'></div>` 这样的元素;
* `//div[contains(@class, 'f1')]`: 获取 `<div class='f f1 f2'></div>` 这样的包含`f1`的元素;
* `//div[@class='job' and @id='job-box']`: 获取`<div class='job' id='job-box'></div>` 这样的元素;
    * `!=`: `price!=9.8`
    * `<`: `price<9.8`, 另有`<=` `>` `>=`等
    * `or`: `price>9.8 or price=9`


属性值
```py
src = htmlElement.xpath("//div[2]//img/@src")[0]
# src是属性值的字符串
```


元素值
```py
name = htmlElement.xpath("//div[2]//span/text()")[0]
# name是包裹的字符串
```


当前元素的子元素
`tr.xpath(".//a/@href")`