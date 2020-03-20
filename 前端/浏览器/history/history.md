### back 和 forward

* `history.back()` : 返回上一页; 
* `history.forward()` : 下一页; 
* `history.go( 页的位置 )` :
  + `history.go(2)` : 后二页; 
  + `history.go(0)` : 本页刷新; 
  + `history.go(-2)` : 前二页; 
* 浏览器加载过的资源, (配置: Date+Cache-Control)浏览器通常直接读取缓存中的数据, 而不是从服务器读取; 

***

### pushState

``` js
window.history.pushState(
    // 第一项参数, 可以通过 history.state 读取
    {
        key1: 'value1'
    },
    '新页面标题, 但没什么用, 可以设为空字符串',
    // 第三项参数, 页面地址, 不能跨域
    '页面地址'
);
```

* 最新的页面是 a 页; 
* 仅在浏览器的历史纪录中新增一条 b 页(在最新处添加, 并不检测是否有效); 
* 浏览器地址栏立刻变成 b 页地址, 但是页面没有跳转或刷新, 内容是 a 页内容; 
* 继续浏览新的地址, 如 `www.baidu.com` 后, 返回, 显示 b 页内容, 通过 `history.state` 读取 pushState 时插入的数据; 
* 继续返回, 显示 a 页内容; 

***

### replaceState

* 仅说明和 pushState 的区别; 
  + 用任意页面替换当前页; 

***

### window.popstate 事件

* 同一个文档的浏览历史变化时, 触发 popstate 事件; 
* `back` , `forwards` , `go` , 方法会触发此事件; 
* `pushState` 和 `replaceState` 不会触发此事件; 

``` js
window.addEventListener('popstate', function(event) {
    console.log('location: ' + document.location);
    console.log('state: ' + JSON.stringify(event.state));
    // history.state === event.state
});

/* 注意: popstate 事件触发后, 默认会滚动文档, 另需设置如下 */
// 阻止默认的"popstate"事件后, 的滚动行为;
if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}

```


