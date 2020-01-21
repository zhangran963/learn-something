注意:

- 尽量在项目本地安装 loader
- 名字写全，如 `style-loader` `css-loader`等；

loader 相关

- babel-loader babel-core babel-preset-es2015 babel-preset-react
- url-loader, file-loader 两个都必须用上。否则超过大小限制的图片无法生成到目标文件夹中

plugin 相关

- `extract-text-webpack-plugin` 把 css 文件生成一个文件,使浏览器单独加载

过程相关
1 `npm init -y` 快速新建 npm 信息
2 `npm install --save-dev webpack`本地载入 webpack

命令

- 运行：webpack
- 安装：`npm install --save-dev css-loader style-loader sass-loader` 等

编译

- `webpack ./js/entry.js ./js/boundle.js` 把源文件编译成新文件(相对当前的路径)

服务器监听

- `webpack-dev-server`
- 注: 若此命令不行,可以设置`npm start`(必须是 start)为`node_modules/.bin/webpack-dev-server`
- `webpack --progress --watch`

`npm install css-loader --registry=https://registry.npm.taobao.org/` 使用淘宝的代理

代码片段

```js
context: path.resolve(__dirname,'src'),
entry: './index.js',
```

js 文件=>页面

```js
new CommonsChunkPlugin({
			name: "commons",
			chunks: ["pageA", "pageB", "admin-commons"],
			minChunks: 2
		}),
```
