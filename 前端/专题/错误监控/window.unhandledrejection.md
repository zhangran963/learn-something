## 专门处理 Promise 的错误

- 规则: 每个 Promsie 都要有自己的 catch
- 建议: 全局再添加一个 unhandledrejection 事件
- 去掉控制台的错误提示: `err.preventDefault()`

```js
/* 监听unhandledrejection事件1 */
window.onunhandledrejection = function(err) {
	console.error('>>> window.onunhandledrejection:', err);

	err.preventDefault(); /* 阻止错误继续传播, 控制台无错误提示 */
};
/* 监听unhandledrejection事件2 */
window.addEventListener(
	'unhandledrejection',
	function(err) {
		console.error('>>> window.addEventListener(onunhandledrejection):', err);
		err.preventDefault(); /* 阻止错误继续传播, 控制台无错误提示 */
	},
	false
);

/* 在Promise生成错误 */
Promise.resolve('data')
	.then(data => {
		data = JSON.parse(data);
	})
	.catch(err => {
		/* catch 中处理掉错误, 不再传递 */
		console.log('>>> Promise.catch:', err);
	});
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9yd6hho1jj316m03ywei.jpg)

### 若没有 .catch 部分

- 错误传递到全局
  ![](https://tva1.sinaimg.cn/large/006tNbRwly1g9yd79mypzj316y0baq3z.jpg)

### 去掉控制台的错误提示: `err.preventDefault()`

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ydb02hnxj316q086aav.jpg)
