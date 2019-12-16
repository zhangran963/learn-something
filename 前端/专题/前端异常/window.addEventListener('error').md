
## 在 html 和 script 中加载的图片
* 只有 `window.addEventListener('error', 回调函数, true)`, 在 **捕获阶段**, 在能获取 `<img src=''>`加载的错误信息, 其余均不能捕获错误信息
```html
<!-- html -->
<img src="/img.png" alt="" srcset="">


<script>
// 事件在前
window.onerror = function (...arg) {
console.log('>>> window.onerror:', { ...arg });
    //   return true
}
window.addEventListener('error', (err)=>{
    console.log('>>> addEventListener error:', err);
}, true)


// 文件请求在后
new Image().src = '/img.png'
</script>
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ycr2y0vnj33340e443m.jpg)