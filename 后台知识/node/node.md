导出和引入的形式
`exports.aaa=xxx` + `var cube=require("./math")` = `cube.aaa`;

`module.exports=xxx` + `var cube=require("./math")` = `cube`;

`export default xxx` + `import cube from '././'` = `cube`

`export function cube(){}` + `export function cubee(){}` + `import {cube,cubee} from '././'` = `cube; cubee;`


### 三种文件路径  
1. `__filename` 输出文件的绝对路径(带有文件名)`E:\nodejs\node包教不包会\node地址外.js`
2. `__dirname` 输出文件的绝对路径(不带有文件名)`E:\nodejs\node包教不包会\lession3`
3. `process.cwd()` 输出执行的文件的 *根文件* 的绝对路径(不带有文件名)`E:\nodejs\node包教不包会`


### RESTful的理解
> URL定位资源，用HTTP动词（GET,POST,DELETE,DETC）描述操作
1. GET    用来获取资源，
2. POST  用来新建资源（也可以用于更新资源），
3. PUT    用来更新资源，
4. DELETE  用来删除资源。
> 综合上面的解释，我们总结一下什么是RESTful架构：  
　　（1）每一个URI代表一种资源；  
　　（2）客户端和服务器之间，传递这种资源的某种表现层；  
　　（3）客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。  
常见错误1.URI包含动词; 2.URI中加入版本号

manifest 文件
配置 `<html manifest="demo.appcache"></html>` + `text/cache-manifest`(服务器配置)


### 计时开始和结束标志
* `console.time()`: 开始计时;
* `console.timeEnd()`: 结束计时;
```
var counter = 10;
console.log("计数：%d", counter);  //关键点1
console.time("获取");
for(var i=0;i<counter;i++){
    i*1.202/8.9*8945;
}
console.timeEnd("获取");   //关键点2，输出："获取: 0.059ms","获取"2字是一个标识符，在timeEnd处打印出来
```

### process 进程，指node执行的进程。
1. `exit` 当进程准备退出时触发；
2. `beforeExit`  监听器可以异步调用，这样 node 就会继续执行。

`util.inherits(constructor, superConstructor)`是一个实现对象间原型继承 的函数。*继承原型，不是继承自身* *原型复制，不是引用的同一个* *在原型中定义的属性不会作为对象的属性输出*

`util.inspect(object,[showHidden],[depth],[colors])`是一个将任意对象转换 为字符串的方法

`util.isArray(object)` 如果给定的参数 "object" 是一个数组返回true，否则返回false。

`util.isRegExp(object)` 如果给定的参数 "object" 是一个正则表达式返回true，否则返回false。

`util.isDate(object)` 如果给定的参数 "object" 是一个日期返回true，否则返回false。

`util.isError(object)` 如果给定的参数 "object" 是一个错误对象返回true，否则返回false。


**文件系统**
`var fs = require("fs")`
* `fs.readFile(url,callBack)`异步读取文件,(err,data),推荐；`fs.readFileSync()`同步读取文件；
* `fs.open(path, flags[, mode], callback)` 在异步模式下打开文件的语法格式
> 1.path - 文件的路径。  
2.flags - 文件打开的行为  
3.mode - 设置文件模式(权限)，文件创建默认权限为 0666(可读，可写)。  
4.callback - 回调函数，带有两个参数如：callback(err, fd)。fd指文件描述符，write或read中可用到

* `fs.stat(path, callback)`获取文件信息
> 1.path - 文件路径。  
2.callback - 回调函数，带有两个参数如：(err, stats), stats 是 fs.Stats 对象。

* `fs.writeFile(filename, data[, options], callback)` 写入文件
> 1.path - 文件路径。  
2.data - 要写入文件的数据，可以是 String(字符串) 或 Buffer(流) 对象。  
3.options - 该参数是一个对象，包含 {encoding, mode, flag}。默认编码为 utf8, 模式为 0666 ， flag 为 'w'  
4.callback - 回调函数*一定会执行*，回调函数只包含错误信息参数(err)，在写入失败时返回。

* `fs.read(fd, buffer, offset, length, position, callback)` 异步读取文件**先open，再read，再close**
> 需新建buffer对象,用于存储读取出的数据

> 1.fd - 通过 fs.open() 方法返回的文件描述符。  
2.buffer - 数据写入的缓冲区。  
3.offset - 缓冲区写入的写入偏移量。  
4.length - 要从文件中读取的字节数。
5.position - 文件读取的起始位置，如果 position 的值为 null，则会从当前文件指针的位置读取。  
6.callback - 回调函数，有三个参数err, bytesRead, buffer; err 为错误信息， bytesRead 表示读取的字节数，buffer 为缓冲区对象。  

* `fs.close(fd, callback)` 关闭文件
> 1.callback - 回调函数，没有参数。

* `fs.ftruncate(fd, len, callback)` 异步模式下截取文件
> 1.len - 文件内容截取的长度。  
2.callback - 回调函数，有参数err。

* `fs.unlink(path, callback)` 删除文件
> 1.path文件路径；
2.callback回调函数，没有参数。

* `fs.mkdir(path[, mode], callback)` 创建目录
> 1.path文件路径；  
2.mode - 设置目录权限，默认为 0777。  
3.callback回调函数，有参数err。

* `fs.readdir(path, callback)` 读取目录
> 1.path目录路径；   
2.callback回调函数，有两个参数err, files，err 为错误信息，files 为 目录下的文件数组列表。

* `fs.rmdir(path, callback)` 删除目录
> 1.path文件路径；  
2.callback回调函数，有参数err。