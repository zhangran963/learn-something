
## `window.onerror`
* 报错源码
![报错源码](https://tva1.sinaimg.cn/large/006tNbRwly1g9yamjrltrj31ac0f9dh7.jpg)
```js
window.onerror = function(...arg){
  console.log('>>> window.onerror:', {...arg});

  /* 用 return true 阻止错误继续传播; err.preventDefault()不能阻止 */
  return true
}

    namee
```

* 返回 true
![](https://tva1.sinaimg.cn/large/006tNbRwly1g9yasbfn1pj32vu0rsn45.jpg)

* 未返回 true
![](https://tva1.sinaimg.cn/large/006tNbRwly1g9yatfi39kj30yy0asmxr.jpg)


## 报错类型
* 能收集的错误
  * 同步
  * 异步: setTimeout等

* 不能收集的错误
  * Promise
  * img 图片
  * 网络请求
  * 网络文件请求(script标签)
