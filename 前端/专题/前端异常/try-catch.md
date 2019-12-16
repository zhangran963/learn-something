## `try...catch...`

* 同步错误
```js
try {
    // 同步
    namee
} catch (err) {
    console.log('>>> try...catch... ', err);
}
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1g9yc9nxddcj30z403ct8n.jpg)


***

* 异步错误
```js
try {
    // 异步
    sleep(1200).then(_ => {
        namee
    })
} catch (err) {
    console.log('>>> try...catch... ', err);
}
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ycbeqlo4j30z803aglk.jpg)

***

* 网络请求
```js
try {
    // 接口
    axios.get('http://localhost:3001/data').then(originData => {
        
        // console.log('>>> :', originData.data);
        let {key} = originData.data1
    })
} catch (err) {
    console.log('>>> try...catch... ', err);
}
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ycdo67u7j30zg03qaa2.jpg)


***

* 静态文件
```js
try {
    // 文件
    new Image().src = '/img.png'
} catch (err) {
    console.log('>>> try...catch... ', err);
}
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ycg5gosij30za02mmx2.jpg)


