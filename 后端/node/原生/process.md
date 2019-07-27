### process 处理
```js
//等待控制台输入
process.stdout.write("请输入用户名:");
//得到输入数据
process.stdin.on('data', (input) => {
    input = input.toString().trim();  // 处理输入的内容
    process.stdout.emit('end');  // 触发其他事件

    process.exit(1)  // 退出
})
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
