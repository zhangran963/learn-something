## 在 html 和 script 中加载的图片

- 只有 `window.addEventListener('error', 回调函数, true)`, 在 **捕获阶段**, 在能获取 `<img src=''>`加载的错误信息, 其余均不能捕获错误信息

```html
<!-- html -->
<img src="/img.png" alt="" srcset="" />

<script>
	/* 尽量放到靠前的位置 */

	window.onerror = function(...arg) {
		console.log('>>> window.onerror:', { ...arg });

		/* 用 return true 阻止错误继续传播; err.preventDefault()不能阻止 */
		return true;
	};

	window.addEventListener(
		'error',
		err => {
			console.log('>>> window.error:', err);

			/* 用 err.preventDefault() 阻止错误继续传播; return true 不能阻止 */
			err.preventDefault();
		},
		true
	);

	// 文件请求在后
	new Image().src = '/img.png';
</script>
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ycr2y0vnj33340e443m.jpg)





