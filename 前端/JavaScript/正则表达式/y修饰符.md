
## y 修饰符, “粘连”(sticky)修饰符。

* 正则表达式的方法, 查找时, 都会从上一次查找结束的地方继续查找, 如 exec, test

***

### g 修饰符, 继续查找, 查找值可不连续
* g 修饰符
![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6nvlg2z2j30qk0feq3e.jpg)

### y 修饰符, 继续查找, 查找值必须是下一个, 否则返回 null
* 因为要求有连续性, y修饰符隐藏了头部匹配的标识`^`
* none
![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6nyoots2j30oa0aydg0.jpg)

* 更改一下正则表达式, 提现出连续性
* `正则表达式.lastIndex`: 下一次查询的起始索引
![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6o82fhvtj30s60hqt92.jpg)


### 检查
* `正则表达式.sticky`: 是否设置了 y修饰符
* `正则表达式.flags`: 修饰符组成的字符串


