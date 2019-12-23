## s 修饰符
* 让`.`能匹配所有的字符


### .
* `.`代表单个字符, 但不包括如下:
  * ![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6p953usyj32p00rs75y.jpg)
* 变通的解决方式: `/foo[^]bar/.test('foo\nbar')`

### s 修饰符
* 使`.`支持所有单字符  
![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6pbdx48nj30f804kq2u.jpg)

### `正则表达式.dotAll`
![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6pctdpcmj30ai04k744.jpg)