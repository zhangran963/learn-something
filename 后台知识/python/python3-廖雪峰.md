`0x`开头: 16进制
***

`print(xxx)` 输出内容;  
`print(r"xxx")` xxx字符串不用转义,直接输出. 如 `print(r"\\\n")`输出`\\\n`;  
用`''' xxx '''`包裹输出多行内容;
```
print('''line1
... line2
... line3''')
```
***

### 判断
```
if age<18:
    print("不能进")
elif age>36:
    print("太老了, 不能进")
else:
    print("please in")
```

* `x is y`判断是否相等, 等同于`x==y`(python不支持===); 
* `x in obj`判断obj是否有x属性;

***

### 输入
`s = input("提示文字: ")` 此函数接受一个输入, 提示文字是`提示文字: `;  
***
### 循环
```
for x in list(range(1,10)):
    print(x);
```
输出 `1,2,3,4,5,6,7,8,9`

```
mylist=[1,2,3,4]
n=len(mylist)
while n>0:
    print(mylist[-n])
    n=n-1
```
输出 `1,2,3,4`

***
### 字典dict( 类似Map)
`mydict = {"xiaoming": 9,"xiaohong": 7, "xiaoliang": 8}`,类似对象,但需要key值用引号包裹.
* `mydict.get("xiaoming")` 查找key值为`xiaoming`的value, 没有返回 `None`;
* `mydict.get("xiaoming",-1)` 查找key值为`xiaoming`的value, 没有返回 `-1`;
* `mydict.pop("xiaoming")` 删除`xiaoming`的内容, 返回`xiaoming`的value;

***
### set ( 类似Set )
* `myset = set([1,3,3,5])`返回`{1,3,5}`, 元素不能重复;
* `myset.add(6)` 添加元素;
* `myset.remove(6)` 删除元素;
* `set1 & set2` 两个set做并集, 取相同元素;
* `set1 | set2` 两个set做交集, 合并元素;
***
### 函数
```
def name(x,n=2):
    print(n)
```
### 函数(默认参数)
`n=2`是默认参数

* 当前两个是必需参数, 后两个是默认参数时,`nenroll('Bob', 'M', 7)` 第三个参数是指定值,第四个参数是默认值; `enroll('Adam', 'M', city='Tianjin')` 第三个参数是默认值,第四个参数是指定值;
### 函数(可变参数)
```
计算多个数的和
def calc(*numbers):
	sum=0
	for c in numbers:
		sum=sum+c
	return sum
```
* `calc(1,2,3)`或`calc( *myTurple )`在list和turple前加星号指此元素作为可变参数;

### 函数(关键字参数)
```
多余的参数变成一个dict
def calc(name,age,**kw):
    print("名称:",name,"年龄:",age,"其他内容:",kw)

```
输入`calc("四叶草",27,city="北京")`输出内容`名称:四叶草 年龄:27 其他内容:{'city':'北京'}`. 也可用`mydict={"city":"北京"}; calc("四叶草",27,**mydict)`指代;

### 生成器
* 生成器用于数列太大的情况, 如果数列太大,有可能超出内存限制. 可以定义生成器(就是规则), 需要用的时候自动生成后面的数;
方法1:
* `(x*x for x in [1,2,3])`这种形式, 就是把数列边缘用`( )`代替;
方法2:
```
# 如果一个函数定义中包含`yield`关键字, 这个函数就是生成器;
# 斐波那契函数, max指代迭代次数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```

***

### 仅在命令行生效
`if __name__=='__main__':` 此段判断代码, 仅会在命令行运行时生效, 在其他如引入时不生效;

 
