### pre-fetch

- prefetch(预取)：将来某些导航下可能需要的资源

  1. prefetch chunk 会在父 chunk 加载结束后开始加载
  2. 浏览器闲置时加载
  3. 用于未来的某个时刻

- 直接在代码最外层中引用时
  - `webpackPrefetch`: 开启 prefetch;
  - `webpackChunkName`: 此预加载的 chunk 的名称;

---

### 无条件加载

```js
import(/* webpackPrefetch: true, webpackChunkName: 'button' */ './LoginButton').then(loginBtn => {
	console.log('* prefetch loginBtn', loginBtn);
});
```

- html 中, 生成主 js 文件

```html
<!DOCTYPE html>
<html lang="zh-cmn">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width,initial-scale=1" />
		<title>[自定义标题] production</title>
		<link href="index.css" rel="stylesheet" />
	</head>

	<body>
		<div id="app"></div>
		<script type="text/javascript" src="vueRouter.chunk.js"></script>
		<script type="text/javascript" src="vueBase.chunk.js"></script>
		<script type="text/javascript" src="index.js"></script>
	</body>
</html>
```

- Element 查看器
  ![直接引用](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225171155.png)

* 网络请求
  ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225172525.png)

---

### 有条件加载

```js
/* 预取 */
prefetch() {
  import(/* webpackPrefetch: true, webpackChunkName: 'button' */ './LoginButton').then(loginBtn => {
    console.log('* prefetch loginBtn', loginBtn)
  })
}
```

- html 中, 生成主 js 文件

```html
<!DOCTYPE html>
<html lang="zh-cmn">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width,initial-scale=1" />
		<title>[自定义标题] production</title>
		<link href="index.css" rel="stylesheet" />
	</head>

	<body>
		<div id="app"></div>
		<script type="text/javascript" src="vueRouter.chunk.js"></script>
		<script type="text/javascript" src="vueBase.chunk.js"></script>
		<script type="text/javascript" src="index.js"></script>
	</body>
</html>
```

- Element 查看器

* 注: `link元素请求`, `as="script"`
  ![html渲染结果](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225173423.png)

- 网络请求
- 注: 请求格式是文本 `text/plain`
  ![网络请求](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225173211.png)

- 执行某事件后
  ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225173739.png)
