### 针对图片资源加载错误
* window的error事件的 捕获阶段;
  * 其他处理方式都不能捕获;
  * 不支持css引入的图片

```js
/* error的捕获阶段, 能获取js加载的图片错误 */
window.addEventListener('error', (err) => {
  console.error('* 捕获图片', err)

  return true
}, true)

sleep(1000).then(_ => {
  let image = document.createElement('img')
  image.src = '/finds.jpg'
  document.body.appendChild(image)
})
```