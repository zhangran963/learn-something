### loader
* `html-loader`可以处理html文件中的图片src地址
* `postcss-loader`+`autoprefixer` 自动添加前缀(配合 postcss.config.js)

## 处理html文件名
---

### 生产环境构建
* `webpack -p`自动把代码压缩

安装
`npm install --save-dev html-webpack-plugin`

1. `plugins: [new HtmlWebpackPlugin()]`
自动生成 index.html 文件;
2. 
```js
plugins: [
    new HtmlWebpackPlugin({
        title: 'My App',
        filename: 'assets/admin.html',
        template: './src/this.html'
    })
  ]
```
配置项: `title:xxxx` `hash:true/false` `filename:'assets/admin.html'` etc;

---

## 清除文件夹
---
安装`npm install clean-webpack-plugin --save-dev`

1. `new CleanWebpackPlugin(['dist'])`

---

## 单独提取某些文件
---
安装`$ npm install extract-text-webpack-plugin --save-dev`

1.

## 导出
1. `module.exports = {       }`;
2. `exports.read = function(){        }`

## 导入
1. `var bar = require("./js2.js")`;
2. `import bar from "./js2.js"`;

## 加载资源文件
1. 加载css文件
```js
module: {
    rules: [
        {test: /\.css$/,use:["style-loader","css-loader"]},
    ]
}
```
2. 加载图片
页面中写法`var myImage = require("../选择器.jpg");`,变量代表<img>的src属性;  
```js
rules:[
    {test: /\.(png|svg|jpg|gif)$/, use: ['file-loader']}
]
```
3. 加载字体文件
rules:[
    {test: /\.(woff|woff2|eot|ttf|otf)$/, use: ["flie-loader"]}
]

### 三种监控模式
1. `webpack --watch`自动编译,但不会自动刷新;
2. `webpack-dev-server`自动编译+自动刷新;还需要在webpack.config.js中配置:
```js
devServer: {
    contentBase: './dist/ht'  /*文件路径*/
},
```
3.


### 多页面的路径处理
* 插件glob
* 可以用此插件读取路径`./src/*/*.js`, 用`数组 = glob.sync( 路径 )`方法获得符合此路径的数组;
