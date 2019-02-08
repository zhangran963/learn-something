### 安装
* 项目中安装, 然后引入;
* `npm install rxjs`

```js
new Observable(subscriber => {
    // 同步产生三条数据
    subscriber.next(1);
    subscriber.next(2);
    subscriber.next(3);
    setTimeout(() => {
        // 异步产生一条数据
        subscriber.next(4);
        subscriber.complete();  // 最后标注结束 complete()
    }, 1200);
}).subscribe({
    next(x){ console.log(x) },
    error(err){ console.log(err) },
    complete(){ console.log('done') }
})
```

### pull 和 push 模式
* pull: Function;
* push: Promise, Observables

|空|生产者(producer)|消费者(consumer)|
|---|---|----|
|Pull(下拉)|被动: 当请求时生产数据|主动: 决定什么时候请求数据|
|Push(推送)|主动: 自己产生数据|被动: 收到数据做响应|