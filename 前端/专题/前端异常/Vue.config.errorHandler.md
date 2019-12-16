## 借用 Vue 的报错函数
* 生产环境也能使用
```js
// 全局配置
Vue.config.errorHandler = (err, vm, info) => {
  console.log('>>> Vue.config.errHandler: err', err);
  console.log('>>> Vue.config.errHandler: vm', vm);
  console.log('>>> Vue.config.errHandler: info', info);
}


// 业务中
    namee
```
![](https://tva1.sinaimg.cn/large/006tNbRwly1g9ydmjfn8xj316q0bmjs9.jpg)

