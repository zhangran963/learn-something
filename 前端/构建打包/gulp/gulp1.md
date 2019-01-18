### 安装
* `npm install -g gulp`;
* `npm install --save-dev gulp`项目本地安装;

### 卸载
* gulp-cli 1.2.2版本能和 gulp4.0.0版本配合;
* `npm install gulp-cli@1.2.2 -g`: 安装gulp-cli;
* `npm install gulp@4.0.0`: 安装gulp;
* gulp-cli不容易清除, 确认 node_modules 中已经删除了 gulp 后, 可以直接清除`/usr/local/bin`中的命令软链接;


### 使用
* 项目下建立`gulpfile.js`文件;
```
var gulp = require("gulp");

gulp.task('default', function(){
    /*做的事情*/
})
```
* 执行`gulp`;
* 名称叫`default`是任务默认值;
* 如果`gulp.task('first'[, 依赖任务数组 ], 回调)`, 命令是`gulp first`;


### 异步/同步
* 默认回调函数里的内容是异步的;
* 如需同步,如下处理;
```
gulp.task("default",['first'] ,function(){
    console.log("default 运行了");
    
});

gulp.task("first",function(cb){
    /* cb 是继续执行的回调 */
    setTimeout(()=>{
        console.log("第一个任务!");
        cb(); /* 执行一下 cb(), 才会继续往下走 */
    },3000);
});

```


### watch
* 监听文件修改;
```
gulp.task("default", function(){
    // 需要有 task, 在运行 watch;
    gulp.watch("files/**/*.js", function (e) {
        e.type;  // added:新增; deleted:删除; changed:改变;
        e.path;  // 路径: /Users/ran/Documents/makepackage/gulpDemo1/files/dir1/one.js
    });
});
```


### 执行
方式1: `gulp --tasks`: 命令执行gulp任务;
方式2: `gulp --gulpfile ./xxx.s`: 用配置文件执行