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