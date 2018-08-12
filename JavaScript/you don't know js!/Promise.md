三种状态:
1. `Pending` 处理中;
2. `Fulfilled` 正常,收到数据了;
3. `Rejected` 错误;

查看Promise属性
`Object.getOwnPropertyNames( Promise.prototype )`这样的属性需要`new Promise()`使用;
`Object.getOwnPropertyNames( Promise )`这样的属性需要`Promise.xxx`使用;

示例:
```
var p = new Promise((resolve, reject)=>{
    // 这里做异步的事;
    setTimeout(()=>{
        // 做完了, 调用resolve( 数据 );
        resolve(23);
    },1000);
});

p.then((data)=>{
    console.log(data);
})
```


### Promise.all( 类数组 );
* 所有promise实例(可能有的不是,直接返回原值)都返回resolve时, 执行then的成功函数;
* 任一promise实例返回inject,整个promise返回 *被inject的promise的值* ;
```
var promise1 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("001");
    },2000);
});
var promise2 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("002");
    },100);
});
var promise3 = 42;  // 直接返回原值;

Promise.all( [ promise1, promise2, promise3] )
.then((dataArr)=>{
    dataArr是三个promise返回的结果组成的数组;
}, (rejectVal)=>{
    rejectVal是被inject的promise返回的值;
})
```

Promise.all()的同步性/异步性
* 同步性: 只有在 promise组 是空时, 首次打印promise是空(没有"pending");
```
var p = Promise.all([])

console.log(p);  // Promise { [] }
// 延时一下;
setTimeout(()=>{
    console.log(p);  //Promise { [] }
});
```

* 异步性: 其他情况都会第一次"penging", 只后才会有结果;
```
var p = Promise.all( [1, 2] );

console.log(p);  // Promise { <pending> }
setTimeout(()=>{
    console.log(p);  // Promise { <pending> }
});
```
```
var promiseArr = [Promise.resolve(44), Promise.reject(55)];
var p = Promise.all( promiseArr );

console.log(p);  // Promise { <pending> }
setTimeout(()=>{
    console.log(p);  // Promise { <rejected> 55 }
});
```



### Promise.race( 类数组 )
* 输入可迭代对象;
* 只要有一个promise返回结果(无论resolve或reject), 就返回此promise;
```
var promise1 = new Promise((accept,refuse)=>{
    setTimeout(accept, 1000, "嘿嘿")
})
var p = Promise.race( [promise1, Promise.resolve("嘿嘿")] );

p.then((data)=>{
    // data: resolve的promise返回的数据
    console.log("1."+data);  // 1.嘿嘿
}, (err)=>{
    // err: reject的promise返回的数据
    console.log("2."+err);
})
```


### async await
* async 用于**函数**, 标识这个函数是异步的(一般的函数都是顺序执行完, 再执行后面的代码);
* await 用于 promise 等可以等待的处理;
    * await 必须和 async 配合使用;
    * 用于 Promise时, 会同步地返回 Promise.then.then... 之后最终的结果;
    * 用于 非Promsie 时, 直接返回 后面的对象(这样好像没啥用);


