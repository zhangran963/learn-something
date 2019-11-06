### 时间
* 输出 某语言, 某时区 的时间
```js
(new Date).toLocaleString('zh-CN', {timeZone: 'Asia/Shanghai'})
//  "2019/11/6 下午3:21:07"
```

### 时区差
```js
// 本地时区差
(new Date()).getTimezoneOffset()
// -480
// 单位: 分
```