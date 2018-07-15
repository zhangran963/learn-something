### 环境


### 多个配置文件
* `webpack-merge`合并多个配置文件用的;

```
** config1: common **
已经有了一个 webpack.common.js

** config2: dev **
const merge = require("webpack-merge");
const common = require("./webpack.common.js");

module.exports = merge(common, {
    ...
});

** package.json **
"scripts": {
    "start": "webpack-dev-server --open --config webpack.dev.js",
    "build": "webpack --config webpack.prod.js"
}
```


### 区分开发和生产环境

```
** config.prob **
const webpack = require("webpack");

plugins: [
    ...
    new webpack.DefinePlugin({
        "process.env.NODE_ENV": JSON.stringify("productionnnn")  // 定义变量, 用于区分开发和生产环境
    })
]

** .js **
process.env.NODE_ENV  //  开发环境:production;  生产环境: productionnnn;
if(process.env.NODE_ENV === "productionnnn"){

}
```


### 代码分离: 手动
```
** config **
entry: {
    // 写多个名字, 可以分成多个代码块;
    index: "./src/index.js",
    another: "./src/anthor.module.js"
},

output: {
    filename: "[name].bundle.js",
    path: path.resolve(__dirname, "dist"),
},
```


### 代码分离: 防止重复
```
** config **
optimization: {
    splitChunks: {
        name: "common"
    }
}




```

