this 不是编写时绑定，而是运行时绑定。它依赖于函数调用的上下文条件。this 绑定与函数声明的位置没有任何关系，而与函数被调用的方式紧密相连。


### 默认情况
* 默认this指代全局变量;函数引用的函数绑定的this也是全局变量
* 函数头部添加"use strict", this不再指定为全局变量;

```
function func(){
    "use strict"
    // this指undefined
    func1()
}

function func1(){
    // this指全局变量
    console.log("func1");
}

func();
```

### 隐含绑定(对象中)

1. 
    * 在对象中引用函数 指代 对象本身;
    * 对象有多层, 指代最小的那个;
    ```
    function func1(){
        console.log(this.name);
    }

    var obj = {
        func1: func1,
        name: "四叶草",
    }
    var objj = {
        name: "er",
        objs: [obj],
    }

    func1();  // this指代全局变量;
    objj.objs[0].func1();  // this指代obj;
    ```

2. 
    * 隐含丢失
    ```
    function func1(){
        console.log(this.a)
    }

    var obj = {
        name: "嘿嘿",
        func1: func1,
    }

    var bar = obj.func1; //引用后,环境丢失
    bar()  // this指代全局;
    ```
3. 
    * `call`或`apply`指明
    ```
    function foo(a,b,c){
        console.log(a, b, c);
    }
    foo.call({name:123}, "first", "second", "third");
    foo.apply({name: 123}, ["first","second","third"]); // 或arguments;
    // call和apply区别在于 是否把参数组成数组;
    ```

    ```
    function foo(a,b,c){
        console.log(this.a, a, b, c);
    }

    var obj = {
        a: 2,
    }
    // 有函数bind, 绑定this用;
    foo.bind(obj)("first");
    // 输出:2, "first"
    ```
4. 
    * `bind`,`call`,`apply`应用的区别;
    ```
    foo.bind(obj)("first","second");

    foo.call(obj,"first", "second");

    foo.apply(obj, ["first", "second"]);
    ```
    * `bind`和`call`区别在于是否执行,仅bind不会执行,后面接()才会执行,如:
    ```
    以下公式相等
    foo.bind(obj)("first", "second", "third");
    foo.bind(obj, "first")("second", "third");
    foo.bind(obj, "first", "second")("third");
    foo.call(obj, "first", "second", "third");
    ```

### 判断规则
```
1. 函数是通过 new 被调用的吗（new 绑定）？如果是，this 就是新构建的对象。

var bar = new foo()

2. 函数是通过 call 或 apply 被调用（明确绑定），甚至是隐藏在 bind 硬绑定 之中吗？如果是，this 就是那个被明确指定的对象。

var bar = foo.call( obj2 )

3. 函数是通过环境对象（也称为拥有者或容器对象）被调用的吗（隐含绑定）？如果是，this 就是那个环境对象。

var bar = obj1.foo()

4. 否则，使用默认的 this（默认绑定）。如果在 strict mode 下，就是 undefined，否则是 global 对象。

var bar = foo() 

```

### function 和 => 区别
```
var obj = {
    time:0
};

function foo(){
    setInterval(function(){
        // 此处this指代全局变量
    },500);
}
foo.call(obj);


function foo(){
    setInterval(()=>{
        // 此处this指代obj
    },500);
}
foo.call(obj);
```


### 复制

浅复制 `Object.assign()`:
```
var o1 = { a: 1 };
var o2 = {a:2,b:2};
var o3 = {a:1,b:2,c:3};

var target = {};

var copy = Object.assign(target, o1,o2,o3);
copy //  {a:1,b:2,c:3}
target //  {a:1,b:2,c:3}
o1,o2,o3//  不变
```