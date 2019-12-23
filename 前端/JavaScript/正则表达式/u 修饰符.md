
## u 修饰符
* `Unicode 模式`: 会正确处理四个字节的 UTF-16 编码。
```js
console.log('>>> without u:', /^\uD83D/.test('\uD83D\uDC2A'));
console.log('>>> with u:', /^\uD83D/u.test('\uD83D\uDC2A'));
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6kyssn7gj30da02amwy.jpg)


### 影响1: 点字符
* 是除了换行符以外的任意单个字符
```js
console.log('>>> . without u:', ('\uD83D\uDC2A').match(/^./))
console.log('>>> . with u:', ('\uD83D\uDC2A').match(/^./u))
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6l4bx2f1j30u604a74h.jpg)


### 影响2: Unicode 字符表示法
> ES6 新增了使用大括号表示 Unicode 字符，这种表示法在正则表达式中必须加上 u 修饰符，才能识别当中的大括号，否则会被解读为量词。
```js
// 按 61个字符串u 匹配
'aaa'.match(/\u{61}/);
// /匹配模式/u 按 Unicode 模式识别字符串
'aaa'.match(/\u{61}/u);
// 按 10个字符串u 匹配
'u'.repeat(10).match(/\u{10}/)
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6n4b10hnj30t808wdg6.jpg)


### 影响3: i修饰符
> 有些 Unicode 字符的编码不同，但是字型很相近，比如， \u004B 与 \u212A 都是大写的 K 。

![](https://tva1.sinaimg.cn/large/006tNbRwly1ga6nocichvj30nu0b0q38.jpg)
* `iu`需要一起添加

