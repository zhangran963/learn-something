### 单js文件
* 指定生成文件名+路径`npx webpack src/index.js --output dist/bundle.js`;

### lodash
```
import _ from 'lodash';

_.join(["Hello", "webpack", "四叶草"] , " * ");
// "Hello * webpack * 四叶草"
```

### 使配置文件
`npx webpack --config webpack.config.js`
```
const path = require("path");

module.exports = {
    entry: "./src/index.js",
    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, "dist")
    }
};
```

### 路径
```
const path = require("path");

path.resolve(__dirname,"dist");
// /Users/ran/Documents/makepackage/demo1/dist
```


### npm脚本
`npm run xxx`: 运行 xxx 代表的内容;


### css
```
** .js **
import "../css/style.css";  // 路径较自由, 相对于 js 文件;

** config **
module: {
    rules: [
        {
            test: /\.css$/,
            use: ["style-loader","css-loader"],
        }
    ]
}
// 这样引入的 css 是通过`<style>  xxx  </style>`包含的, 在 html 中;
```

### 分离的 CSS 文件
* `extract-text-webpack-plugin`生成单独 CSS 文件的插件;
```
** config **
rules: [
    {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
            fallback: "style-loader",
            use: "css-loader"
        })
    }
]
...
plugins: [
    new ExtractTextPlugin("styles.css");
]

** .js **
import "./style.css";
```

### 图片
```
** js **
import Icon from "./icon1.png";  //图片

var myIcon = new Image();
myIcon.src = Icon;  //引入的图片作为 src 引入
element.appendChild( myIcon );

** config **
// css 和 图片 的验证在同级
// css样式对文件有作用
rules: [
            {// css 文件
                test: /\.css$/,
                use: ["style-loader","css-loader"],
            },{// 图片文件
                test: /\.(png|svg|jpg|gif)$/,
                use: ["file-loader"]
            }
        ]
```

### 数据


```
** config **
rules: [
    ...
    ,{
        test: /\.xml$/,
        use: ["xml-loader"]
    }
]

** xml数据 **
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Mary</to>
  <from>John</from>
  <heading>Reminder</heading>
  <body>Call Cindy on Tuesday</body>
  <hehe>嘿嘿嘿嘿</hehe>
</note>

** .js **
import Data from "./data.xml";

Data;  // 对象形式
Data["note"];  // 对象的属性

```


### 多js文件入口
```
*** html **
// 提前引入文件
<script src="./print.bundle.js"></script>
<script src="./app.bundle.js"></script>

*** config **
entry: {
        // 2个文件入口, 属性名 用于输出文件;
        app: "./src/index.js", 
        print: "./src/print.js"
    },
    output: {
        // 输出文件会按 对应属性名输出
        filename: "[name].bundle.js",
        path: path.resolve(__dirname, "dist")
    },

```

### 修正 html
插件: `html-webpack-plugin`;
* 自动生成 index.html; 自动添加 "script";
```
** config **
const HtmlWebpackPlugin = require("html-webpack-plugin");

plugins: [
        new HtmlWebpackPlugin({
            title: "输出 Management"  // 替换 html中的<title>内容;
        })
    ]
```


### 清除旧数据
插件: `clean-webpack-plugin`;
* 写入之前先把旧数据清除;
```
*** config **
plugins: [
    new CleanWebpackPlugin(["dist"]),  // 清除 dist 文件夹下的内容;
]
```

### 代码精简
插件: `uglifyjs-webpack-plugin`;
* 可以精简掉没有用到的 function,
```
** config **
const UglifyJSPlugin = require("uglifyjs-webpack-plugin");

plugins: [
    ...
    new UglifyJSPlugin(),
]


```

### 显示源文件输出行数(开发中)
* `devtool: "inline-source-map"`
```
** config **
// 启用输出源文件行数功能;仅开发用;
devtool: "inline-source-map",
```



### 文件监听功能1
* `webpack --watch`; 文件更改后就编译;但需手动刷新;

### 文件监听功能2
* `webpack-dev-server --open`, 服务运行在`http://localhost:8080`; 文件更改后就编译; 会自动刷新;
```
** config **
devServer: {
    contentBase: "./dist"
}
```

### 文件监听功能3
* 中间件    



### 模块热替换
* 自动更新部分模块, 不用刷新;
* 应用效果并不理想;
```
** config **
const webpack = require("webpack");

devServer: {
    contentBase: "./dist",
    hot: true,   // 添加 true
},
plugins: [
    ...
    new webpack.NamedModulesPlugin(),
    new webpack.HotModuleReplacementPlugin()
]

** .js **
...
if(module.hot){
    module.hot.accept("./print.js", function(){
        console.log("print.js 文件改变了;");
    });
}

```


###