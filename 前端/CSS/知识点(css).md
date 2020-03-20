#### box-sizing:

01. content-box:使width和height仅包括内容(默认)
02. border-box:宽度+padding+border；

#### 私有属性的定义

* Firefox: -moz-  
* opera: -o-     
* chrome/safari: -webkit-
* ie:-ms-

#### box-orient

> 1.horizontal/inline-axis  水平排列；

02. vertical   垂直排列；
03. inherit    继承自父元素；
04. block-axis   垂直排列；

``` 
ul{
    display: -webkit-box;
    box-orient: horizontal;
}
```

#### box-direction

01. normal  默认，按HTML的文档顺序显示；
02. reverse  反向显示；

``` 
ul{
    display: -webkit-box;
    box-direction: reverse;  // 3,2,1排列
}
```

#### box-align 垂直方向

01. start  顶部对齐；
02. end   底部对齐；
03. center  垂直居中对齐；
04. stretch  拉伸，使子元素与父元素等高(兼容性不太好)；

#### box-pack 水平方向

01. start  左对齐；
02. end  居中对齐；
03. center  垂直居中对齐；
04. Justify  两段对齐，水平等分父元素高度；

box-shadow: x轴偏移, y轴偏移, 模糊距离, 放大的尺寸, 颜色; 

outline: 宽度 | 样式 | 颜色 ; 

> 不占据空间; 在border外，类似border; 

table表格中，td属性加上 `colspan="4"` ，代表合并4项

word-wrap:break-word; 允许断句子，单词在下一行；
word-break：break-all; 断全部，单词连下一行都不用去了(更彻底)；
white-space:pre; 指怎么显示空白，pre 指现在是写的怎么样就怎么显示；

文本两端对齐

> `text-align:justify;` 

编辑

> contenteditable 可以编辑内容，设置contenteditable为true；

meta知识点

01. `<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />` 优先使用IE最新版本 和 Chrome; 
02. `<meta http-equiv="X-UA-Compatible" content="IE=8" />` 使用IE8
03. `<meta http-equiv="renderer" content="webkit|ie-comp|ie-stand" />` 控制使用哪种内核; 
04. `<meta http-equiv="Cache-Control" content="no-siteapp" />` 避免转码
05. `<meta name="keywords" content="李先生,何首乌,老司机,MR_LP" />` 页面关键字
06. `<meta name="description" content="我每天都承受着这个年纪不应该有的帅气，我好累" />` 页面描述
07. `<meta name="robots" content="index,follow" />` all: 文件可检索，链接可查询; none: 文件、链接不可用; index: 文件可检索; follow: 链接可查询; noindex: 文件不可检索; nofollow: 链接不可查询; 
08. `<meta name="refresh" content="0;url=http://blog.csdn.net/mr-lp/article/details" />` (content内的数字'秒'后)，刷新，有url时，会重定向到指定的网页; 
09. `<meta name="Expires" content="Mon,12 May 2016 00:20:00 GMT" />` 网页过期时间; 

**下面是移动端部分**

10. `<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no" />` 其他有minimum-scale
11. `<meta name="apple-mobile-web-app-capable" content="yes" />` 启用WebApp 全屏模式
12. `<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />` 开启WebApp全屏模式时生效，取值 default/black/black-translucent
13. `<meta name="apple-mobile-web-app-title" content="标题内容" />` 添加到主屏后的标题
14. `<meta name="format-detection" content="telephone=no" />` 忽略数字自动识别为电话号码
15. `<meta name="format-detection" content="email=no" />` 忽略自动识别邮箱

### 解决浏览器滚动条有没有时, 内容跳动问题

``` 
html {
    overflow-y: scroll;
}
:root {
    overflow-y: auto;
    
    overflow-x: hidden;
}
:root body {
    position: absolute;
}
body {
    width: 100vw;
    overflow: hidden;
}
```

### 子元素跟随父元素高度 

``` 
父元素:{
    min-width: calc(100vh - 150px);
    # 设置最低高,防止父元素过低;
    position: relative;
}

子元素(左-侧边栏):{
    position: absolute;
    top: 0;
    bottom: 0;
    # 让左边栏跟随父元素高度;
}
子元素(右-内容区):{
    /*正常编辑,内容多时,可以撑开父元素*/
}
```

