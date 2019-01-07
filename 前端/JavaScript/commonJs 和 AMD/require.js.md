浏览器这种写法:
```
<script src="1.js"></script>
<script src="2.js"></script>
<script src="3.js"></script>
```
* 加载的时候, 网页停止渲染, 文件越多, 失去响应的时间越长;
* js文件之间存在依赖性, 依赖性强的需要放到最后, 当关系复杂的时候, 代码维护困难;

### require.js 的目的
1. 实现 js文件的异步加载, 避免网页失去响应;
2. 管理模块间的依赖性, 便于代码编写和维护;

### 尽量避免网页失去响应的方式
1. 把`<script src="js/require.js"></script>`放在页面底部;
2. 设置`<script src="js/require.js" defer async="true"></script>`;

*** 

### 开始应用
1. 用 require.js 引入 js 文件,`<script src="js/require.js" data-main="js/main"></script>`
    * `data-main="js/main.js"`指定网页程序的主模块;
    * ``





### 独立模块
2种写法
1. 
```
define({
    add: function (x,y){
        return x+y;
    }
})
```
2. 更自由一点,可以初始化数据  
```
define(function(){
    var add = function( x, y){
        return x+y
    }

    return {
        add: add
    }
})
```

### 非独立模块
引入的模块还依赖其他模块
```
/* 主模块 */
require(['math'], function(mm){
    console.log(mm.add(1,2)) 
});

/* 主模块引入这个模块, 这个模块再引入pow */
define( ["pow"], function(pow){
    var addPow = function( x, y){
        return pow.pow(x)+pow.pow(y);
    }

    return {
        addPow: addPow
    }
})

/* pow模块 */
define({
    pow: function(n){
        return n*n;
    }
});
```