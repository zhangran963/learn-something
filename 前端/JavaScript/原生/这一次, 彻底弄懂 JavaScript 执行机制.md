[文章链接](https://juejin.im/post/59e85eebf265da430d571f89)

# 两个大分类: 同步任务 & 异步任务
* 同步任务: 网页渲染主流程是一大堆同步任务;
* 异步任务: 网页中的 图片/音乐/css链接等就是异步任务;


# 流程图
![流程](https://user-gold-cdn.xitu.io/2017/11/21/15fdd88994142347?imageView2/0/w/1280/h/960/ignore-error/1)
* 同步任务直接按顺序执行
* 异步任务进入 Event Table & 注册函数;
* 异步任务 执行中...;
* 



# setTimeout
* 把回调函数加入到 Event Queue 中;
* 经过指定的时间后, 把回调函数加入 主线程;
* 有可能主线程正在做某些事, 所以得等这事做完, 再执行回调函数;
* setInterval 每隔固定的时间, 把回调函数加入主线程 (一旦setInterval的回调函数fn执行时间超过了延迟时间ms，那么就完全看不出来有时间间隔了);


# promise.nextTick(callback)
* 事件循环的下一次循环中, 调用 callback 回调函数;

# macro-task(宏任务) & micro-task(微任务)
* macro-task: 整体 script, setTimeout, setInterval
* micro-task: Promise, process.nextTick
* 同一类型的任务进入同一 Event Queue;


# 执行过程
1. 进入整体代码(宏任务), 开始第一次循环;
2. 执行所有微任务;
3. 执行 **一个排在前面的** 宏任务;
4. 执行所有微任务;
5. ...
6. 没有宏任务和微任务, 不再执行(监听中...);




```js
console.log('1');

setTimeout(function() {
    console.log('2');
    process.nextTick(function() {
        console.log('3');
    })
    new Promise(function(resolve) {
        console.log('4');
        resolve();
    }).then(function() {
        console.log('5')
    })
})
process.nextTick(function() {
    console.log('6');
})
new Promise(function(resolve) {
    console.log('7');
    resolve();
}).then(function() {
    console.log('8')
})

setTimeout(function() {
    console.log('9');
    process.nextTick(function() {
        console.log('10');
    })
    new Promise(function(resolve) {
        console.log('11');
        resolve();
    }).then(function() {
        console.log('12')
    })
})
```

* 结果`1，7，6，8，2，4，3，5，9，11，10，12`