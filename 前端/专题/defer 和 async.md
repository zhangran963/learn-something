- defer 和 async 都是用到 `<script>` 标签上的属性

### defer

* 延后到 `文档完全被解析和显示` 之后再执行, onload事件之前; 只对外部脚本文件有效; 

``` html
<body>
    页面内容
    <script>
        window.onload = function() {
            console.log('* ', 'window.onload');
        };
        /* 卸载前, 执行 */
        // window.onbeforeunload = function(){
        //   console.log('* ', 'onbeforeunload')
        // }
    </script>
    <script src="./1.js"></script>
    <script src="./2.js" defer></script>
    <script src="./3.js"></script>
    <script src="./4.js"></script>
    <script src="./5.js"></script>
</body>
```

![结果](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200118160642.png)

***

### async

* 异步加载脚本, 但不应妨碍页面中的其他操作, 如下载文件, 解析文件等

``` html
<body>
    页面内容
    <script>
        window.onload = function() {
            console.log('* ', 'window.onload');
        };
        /* 卸载前, 执行 */
        // window.onbeforeunload = function(){
        //   console.log('* ', 'onbeforeunload')
        // }
    </script>
    <script src="./1.js"></script>
    <script src="./2.js" async></script>
    <script src="./3.js"></script>
    <script src="./4.js"></script>
    <script src="./5.js"></script>
</body>
```

![结果1 chrome](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200118162006.png)

![结果2 firefox](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200118162106.png)

