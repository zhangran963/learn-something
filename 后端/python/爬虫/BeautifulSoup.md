* 引入`from bs4 import BeautifulSoup`
* 实例化一个对象`mybs = BeautifulSoup(targetHtml)`

### Tag
* `mybs.prettify()`格式化一下内容;
* `mybs.title` 获取title段HTML;
* `mybs.head` head段HTML;
* `mybs.a` 获取第一个a元素;
* `mybs.a.name` 返回`a`;
* `mybs.a.attrs` 获取属性字典;
* `mybs.a.attrs['href']` | `mybs.a.get('href')`读取具体某一属性;

### NavigableString
* `mybs.a.string`获取文本内容;


### Comment
* `mybs.a.string`会输出注释内容;
处理方式:
```
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
```

### find_all 查找函数
* `mybs.find_all(id='likes')` 返回list, 通常仅一项;
* `mybs.find_all(class_='likes')` 返回list;(class是Python中的关键字,需要写成class_);
* `mybs.find_all(attrs={'class':'likes'})` 返回list;
* `mybs.find_all(text=re.compile('^精品'))` 返回list,只有文字内容;

### select 查找函数
* `mybs.select("a")` 返回list
* `mybs.select(".css")` 返回list
* `mybs.select("#css")` 返回list


* `mybs.get_text()` 获取文本内容;

