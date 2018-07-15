* `ctrl+z+enter` 退出命令行
* `print()` 打印功能;
* `r'xxxx'` 在字符串前加字母r, 可以省略掉转义字符;
* `and` `or` `not` 与 或 非 运算符;

### list
* `range(4,10)` 生成4到9组成的list;
* `[x*x for x in range(1,11)]` 生成1到10组成的list,每个元素是x*x ;
* `[x * x for x in range(1, 11) if x % 2 == 0]` 用`if x%2==0`添加偶数的限制条件;
* `[m+n for m in 'ABC' for n in 'abc']`=>`['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']` 多层表达式,生成复合列表;

* `list` 类似数组,可以倒序访问,如`mylist[-1]`;
* `len(xxx)` 获取xxx的长度;
* `mylist.append("xxx")` 往list中添加数据;
* `mylist.insert(index,"xxx")` 在index位置插入数据;
* `mylist.pop()` 从最后弹出一条,返回弹出的数据;
* `mylist.pop(index)` 弹出index位置的数据,返回弹出的数据;
* `mylist.sort()` 相同类型的元素, 可以进行sort排序;

### list的切片操作
* `mylist[0:3]` 取索引为0到2的值. 如果开始索引是0,可写成`mylist[:3]`. `mylist[:]`指复制一个数组;
* `mylist[::n]` 第三个变量n指每n个元素取出一个值;
* `mylist[-2:]` 倒序切片,倒数第二个元素到最后元素;
* `mylist[-4:-1:2]` 倒序切片,倒数第二个元素到倒数第一个元素,每2个取一个值;



* `t = ('Adam', 'Lisa', 'Bart')` 元组tuple,定义之后不能修改;
* `t=("first",)` 创建包含一个元素的元组,添加一个逗号,使与运算符区分;
* `m = ({"name":"ran","age":26},)` 元组中的对象属性名可添加,属性值可以改变;
* if elseif else 的结构是:
```
    if xxx:
    elif xxx:
    else:
```

* for循环的结构是:
```
for val in arr:
    xxx
```  

* 变量`max`是预定义值;
* `d = {"Adam":59,"Lisa":85,"Bart":59}` dict类,类似对象,键值对形式,用`len()`获取长度;
* 判断属性名'xxx'是否在d中;
1. `if 'xxx' in d:`
1. `d.get('xxx')` 若不存在返回None;
* `for key in d` 循环d;
* `for val in d.values()` 其中`.values()`把d转换成list,再循环;
* `for val in d.itervalues()` 其中`.itervalues()`依次在d中取出值,再循环;
* `for key,val in d.items()` 其中`.items()`依次在d中取出key和val,再循环;
* `for key,val in d.iteritems()` 其中`.iteritems()`依次在d中取出key和val,再循环;


* `s = set(['A', 'B', 'C'])` 创建时:用`set()`方法,传入一个list;
* `'xxx' in s` 判断xxx是否在s中;
* `s.add(xxx)` 把xxx添加到s中,重复不报错;
* `s.remove(xxx)` 把xxx从s中移除,没有时报错;

### 函数
* `abs(xxx)` 绝对值
* `max(xxx,xxx,xxx...)` 最大值;
* `int("xxx")` `float("xxx")` `str("xxx")` `bool(xxx)` 类型转换;
* `hex(xxx)` 把xxx转换为16进制;
* `cmp(x,y)` 1.x<y:-1 2.x=y:1 3.x>y:1 ;
* `int(xxx,[num])` 把xxx转换成整数,num指明进制数;
* `str(xxx)` 把xxx转换成字符串;
* `power(x,a=2)` 通过指明a=2,设置a的默认值是2;
* `power(*arg)` 通过变量前加上星号代表可变参数,内部会转换成元组形式,可指代0到任意多个元素;

***
### 定义函数
* `def myFunc(x):` 定义函数
```
def myabs(x):
	if(x>=0):
		print("no")
	else:
		print(abs(x))
```
* `return x,y` 可以返回多个元素, 自动组成元组`(x,y)`;

***
### 迭代(循环)
* `for name in list:` 取出元素本身,非索引;
* `for index,value in enumerate(mylist):` 通过enumerate()函数同时取出索引和元素/key. 实际内部操作是:
```
for t in enumerate(L):
    index = t[0]
    name = t[1]
    print index, '-', name

```

***
### 迭代(对于dict)
* 默认形式: 取dict的key, `for x in mydict:`
* 取dict的item, `for item in mydict.items():`
* 取dict的值, `for x in mydict.values():`
* 取dict的key和value, `for k,v in mydict.items()`

*** 
### 判断是否可以迭代
```
# 引入依赖
from collections import Iterable
# 判断
isinstance([1,2,3],Iterable)

```

***
### 其他
* `pass` pass语句什么都不做,可用于占位符;
* ``

***
### 匿名函数
`lambda x: x*x`等于`def aa(x): return x*x`
* 用法`list(map( lambda x:x*x, [1,2,3,4,5]))`

### 装饰器
```
# 定义装饰器
def log(func):
    def wrapper(*args, **kw):
        print('调用了 %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 使用装饰器
@log
def now():
    xxx
```
`now()`等效于`now = log(now)`

### 偏函数
* 把一个函数的某些值固定住,组成一个新函数;
```
import functools  # 引入函数工具
intx = functools.partial(int, base=5)  # 定义偏函数
intx("1234")  # 使用偏函数
```

### 定义类
```
# 定义
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__hei__ = [1,2,3]
    def printxxx(self):
        print("%s的成绩是%s" % (self.name, self.score))
# 实例化
siyecao = Student("四叶草",68)
# 调用
siyecao.printxxx()
```
* 定义时, 没有指定的类别, 都会填写object;
* 都会有`__init__`函数, 用于初始化此函数, 第一个变量`self`指class自身;
* 类内部的变量如果用`__`开头, 外部不能访问, 如`self.__name = name`;
* 特殊:以`__xxx__`表示的变量是特殊变量,外部可以直接访问;
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
