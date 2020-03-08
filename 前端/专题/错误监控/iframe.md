- 父元素

```html
<!-- html -->
<iframe src="./index copy.html" frameborder="0"></iframe>

<script>
	// window.frames需要放到 iframe 后面, 保证脚本能获取到此元素
	window.frames[0].onerror = function(...arg) {
		console.log('iframe', { ...arg });
		// return true;
	};
</script>
```

- iframe 中

```html
<script>
	// 同步
	namee;
</script>
```

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ydzync46j32mp0rs7az.jpg)
