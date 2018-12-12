**读取文件**
1. `fs.readFileSync("xxx.txt")`同步读取，阻塞
2. `fs.readFile("xxx.txt",function(err,data){  })`异步读取，非阻塞
> 注：`err`在前，如果在读取文件过程中发生错误，错误 err 对象就会输出错误信息。`data`在后；

**引入xxxxx模块**  
`var namexxx = require("xxxxx");`
```js
// 引入 events 模块
var events = require('events');
// 创建 eventEmitter 对象
var eventEmitter = new events.EventEmitter();
```

**EventEmitter的属性(同emit)**
1. `addListener(event,listener);`添加一个监听器到监听器数组的尾部
2. `once(event, listener)`监听器最多只会触发一次，触发后立刻解除该监听器。
3. `removeListener(event, listener)`移除指定事件的某个监听器
4. `removeAllListeners([event])`

**绑定事件处理程序**  
`eventEmitter.on("eventName",eventHandler);`

**触发事件**  
`eventEmitter.emit("eventName" [,arg1] [,arg2] ...);` 关键在`.emit()`,绑定事件,后面的参数依次作为回调函数的参数
eventName可以是connection/data_received等；

**Buffer(缓冲区)**
> 存二进制数用的，例如：暂时存储一下文件；
1. `var buf = new Buffer(10)`
2. `var buf = new Buffer([10, 20, 30, 40, 50]);`
3. `var buf = new Buffer("www.runoob.com", "utf-8");`通过一个字符串来创建 Buffer 实例
4. `len = buf.write("www.baidu.com")`写入
5. `buf.toString([encoding[, start[, end]]])`读取
6. `buf.toJSON()`转换为JSON对象
7. `Buffer.concat(list[, totalLength])`缓冲区合并
8. `buf.compare(otherBuffer);`返回一个数字，表示 buf 在 otherBuffer 之前，之后或相同。
9. `buf.copy(targetBuffer[, targetStart[, sourceStart[, sourceEnd]]])` 缓冲区拷贝,没有返回值，buf复制到targetBuffer
10. `buf.slice([start[, end]])` 缓冲区裁剪
11. `buf.length;`

**Stream(流)**
> 从流中读取数据
```js
var fs = require("fs");
var data = '';

var readerStream = fs.createReadStream('input.txt');

readerStream.setEncoding('UTF8');

readerStream.on('data', function(chunk) {
//读取时，都需要这样处理一下
});

readerStream.on('end',function(){
   console.log(data);
});
```

> 写入流(1.创建文件的流；2.写入)
```js
var fs = require("fs");
var data = '菜鸟教程官网地址：www.runoob.com';

var writerStream = fs.createWriteStream("output.txt")
writerStream.write(data,"utf-8");
writerStream.end();
```

> 管道(复制用)
```js
var fs = require("fs")

var readerStream = fs.createReadStream("xxx.txt")
var writerStream = fs.createWriteStream("output.txt")

readerStream.pipe(writerStream)
```

> 链式流
```js
var fs = require("fs");
var zlib = require('zlib');

fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('input.txt.gz'));
 //读取，压缩，保存
```
