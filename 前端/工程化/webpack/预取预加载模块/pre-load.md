### pre-load

- preload(预取)：将来某些导航下可能需要的资源

  1. 在父 chunk 加载时，以并行方式开始加载
  2. 中等优先级, 立即下载
  3. 用于当前时刻

- 直接在代码最外层中引用时
  - `webpackPreload`: 开启 preload;
  - `webpackChunkName`: 此预加载的 chunk 的名称;

---

### 无条件加载

```js
import(/* webpackPreload: true, webpackChunkName: 'button' */ './LoginButton');
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
  ![直接引用](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225174900.png)

* 网络请求
  ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225175127.png)

---

### 有条件加载

```js
/* 预加载 */
preload() {
  import(/* webpackPreload: true, webpackChunkName: 'button' */ './LoginButton').then(loginBtn => {
    console.log('* preload loginBtn', loginBtn)
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
  ![html渲染结果](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225180007.png)

- 网络请求
  ![默认网络请求](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225175602.png)

- 网络请求(执行条件后)
  ![执行条件后的网络请求](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200225175826.png)
