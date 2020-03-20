### 对IE浏览器的js处理

``` html
<!--[if IE 8]> ie8 <![endif]-->

<!--[if IE 9]> 骚气的 ie9 浏览器 <![endif]-->
```

***

### 判断Safari浏览器

``` js
/* Safari */
let isSafari = /a/.__proto__ == '//';
```

***

### 判断Chrome浏览器

``` js
/* Chrome */
let isChrome = Boolean(window.chrome);
```

