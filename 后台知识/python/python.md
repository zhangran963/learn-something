* 定义类时,添加`__slots__ = ("name","score","age","__hei__")`,表示只允许标识的类添加;
* 定义类时,添加`def __str__(self): return "你调用的是: %s !" % self.name`,表示打印实例(`print( shili )`)时的对应功能

### 正则表达式
```
import re
re.match(r'正则式', 字符串)
# 返回match对象, 需要bool()查看True或False 
```
`re.split(r'\s+',"a b   c d")`按空格分割成list
* 分组
```
m = re.match(r'^(\d{1,3})-(\d{6,7})')
m.groups() # 匹配内容按组划分组成的元组;
m.group(0) # 匹配的全部内容;
m.group(1) # 第一组的内容;
m.group(2) # 第二组的内容;
```

### datetime模块
* `from datetime import import`引入模块;
* `datetime.now()`获取现在时间`2018-01-22 16:18:38.195574`;
* `datetime.now().day`获取日期, 类似有`.month`,`.year`,`.date()`等;
* `datetime(2017,12,9,12,23)`设置时间;
* `datetime(2017,12,20).timestamp()`获取时间戳;
* `datetime.fromtimestamp(xxx)`把时间戳转换成日期;
* `datetime.strptime("2017-6-1 18:19:59","%Y-%m-%d %H:%M:%S")`按设置的时间格式, 把字符串处理成时间;
* `datetime(xxx).strftime("%y-%m-%d %H:%M:%S")`把时间对象按设定的格式输出,
* `from datetime import datetime,timedelta`引入时间模块和时间加减模块;
* `datetime(xxx)+timedelta(days=1,hours=12)`方便算出之前之后的时间;
