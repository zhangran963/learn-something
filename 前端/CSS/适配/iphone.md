### 滚动流畅
* iphone 浏览器中添加`-webkit-overflow-scrolling: touch;`


### 底部横杠
* 类 iphoneX 屏幕
```html
<meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=no, viewport-fit=cover" />
```
```css
padding-bottom: env(safe-area-inset-bottom);
padding-bottom: constant(safe-area-inset-bottom);
```