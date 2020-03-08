### `try...catch...`

- 同步错误
  - 被捕获的错误, 不会继续传播

```js
try {
	// 同步
	namee;
} catch (err) {
	console.log('>>> try...catch... ', err);
}
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9yc9nxddcj30z403ct8n.jpg)

---

- 异步错误

```js
try {
	// 异步
	sleep(1200).then(_ => {
		namee;
	});
} catch (err) {
	console.log('>>> try...catch... ', err);
}
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ycbeqlo4j30z803aglk.jpg)

---

- 网络请求

```js
try {
	// 接口
	axios.get('http://localhost:3001/data').then(originData => {
		// console.log('>>> :', originData.data);
		let { key } = originData.data1;
	});
} catch (err) {
	console.log('>>> try...catch... ', err);
}
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ycdo67u7j30zg03qaa2.jpg)

---

- 静态文件

```js
try {
	// 文件
	new Image().src = '/img.png';
} catch (err) {
	console.log('>>> try...catch... ', err);
}
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ycg5gosij30za02mmx2.jpg)

---

### 报错类型

- 能收集的错误

  - 同步

- 不能收集的错误
  - 异步
  - 网络请求
  - 网络文件请求
