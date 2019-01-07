v-once 一次性地插值
> <span v-once>This will never change:{{msg}}</span>

HTML属性中使用v-bind绑定，用`:`简写

使用过滤器  
```
var a = new Vue(){
    el:,
    data:{},
    filters:{
        capitalize:function(value){    }
    }
}
```

> 过滤器默认接受表达式值作为第一个参数。  
`{{ message|filterA|filterB }}`


v-bind缩写`<a :href="url"></a>`  
v-on缩写`<a @click="dosomething"></a>`

watch
> 只要watch的关键字发生变化，就执行相应的function；

在内联语句处理器中访问原生 DOM 事件。可以用特殊变量 $event 把它传入方法：
>
```
<button v-on:click="warn('Form cannot be submitted yet.', $event)">Submit</button>
```

event.preventDefault()


给数组的某一项改变新值（会更新）
```
Vue.set(example1.items, indexOfItem, newValue);
example1.items.splice(indexOfItem, 1, newValue);
```


推荐用事件修饰符代替原生js语句
> `.stop` `.prevent` `.capture` `.self` `.once`  
代替`event.preventDefault()` `event.stopPropagation()`  
语句：`<a v-on:click.stop.prevent="doThat">tyru</a>`

按键修饰符
> 缩写：`<input v-on:keyup.enter="submit">` 缩写为
`<input @keyup.enter="submit">`  
全部按键别名：`.enter` `.tab` `.delete` `.esc` `.space` `.up` `.down` `.left` `.right` `.ctrl` `.alt` `.shift` `.meta`  
自定义修饰符：`Vue.config.keyCodes.f1 = 112`

创建组件
```
Vue.component('my-component',{

});
```

自定义标签：小写+包含一个横杠(建议)

**Vue-router**
1. `$route.params` 读取路由的自定义值,使用方式`$route.params.id`等
2. `const app = new Vue({
  router
}).$mount('#app')` 给页面嵌套加上路由
