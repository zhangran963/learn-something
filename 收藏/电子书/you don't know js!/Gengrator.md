### generator(生成器)

星号写在哪里都行;
`function*foo(){ }` `function *foo(){ }` `function* foo(){ }`

示例:
```
var x=1;

function *foo(){
    x++;
    yield;
    console.log(x);
}

var it = foo();  //构建迭代器;
it.next();  //执行foo函数的yield前段;
// 被yeild隔断;
it.next();  //执行foo函数的yield后段;
```

返回值
```
function *foo(x,y){
    return x*y;
}
let it = foo(6,7);  //构建迭代器,并填充预设值;
let result = it.next();  //{ value: 42, done: true }
result.value  //42
```

设置值
```
function *foo(x){
    var result = x*(yield);  //设置断点;
    result = result - (yield);  //
    return result;
}
let it = foo(2);  //设置迭代器+预设值(6);
it.next();  //开始执行(第一段);
it.next(3);  //赋值+执行第二段; { value: undefined, done: false}
it.next(1);  //赋值+执行第三段; { value: 5, done: true}
```

> 第一个`.next()`总是启动一个geneator, 运行至第一个`yield`, 第二个`.next()`需要满足第一个`yield`的条件, 以此类推;



```
function *foo(x){
    var result = x*(yield "回传消息");
    return result;
}

var it = foo(2);
it.next();  //{value: "回传消息", done: false}
it.next(3);  //{value: 6, done: true}
```