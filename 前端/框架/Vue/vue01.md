### created 实例创建后执行钩子
```
created: function(){

}

/** 或 **/
created(){

}

/*不要用箭头函数*/
created: ()=>{
    这里的 this, 指代 window
}
```

* Vue声明周期
![image](https://cn.vuejs.org/images/lifecycle.png);

