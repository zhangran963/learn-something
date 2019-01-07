* 获取元素节点: `HTMLElement.childNodes[0]`,`HTMLElement.childNodes[2].childNodes[0]`;
* 设置节点样式: `HTMLElement.childNodes[0].style.border = '1px solid green'`;
* 获取子节点数组(只获取子节点,不获取子文本内容): `HTMLElement.children`;
* 获取父节点: `HTMLElement.parentNode`直接获取父节点, 没有数组;
* 父节点设置样式: `HTMLElement.parentNode.style.border = '1px solid green'`;
* 用对象的形式读取DOM属性: `document.getElementsByTagName('img')[0].src`, `document.getElementsByTagName('img')[0].style.width`;
* 获取 class: `document.getElementsByTagName('img')[0].className`;
* 获取计算后的样式: `window.getComputedStyle( document.getElementsByTagName('img')[0] ).borderWidth `;
* 创建插入节点: 
```
var li = document.createElement("li");
var text = document.createTextNode("我就是创建的文字;");
li.appendChild( text );
document.getElementsByTagName("ul")[0].appendChild( li );
```

* 删除节点:
```
var lis = document.getElementsByTagName("li");
var li = lis[ lis.length-1 ];
li.parentNode.removeChild( li );  // 移除;
```


### 赋值作用域
```
function a(){   }  //全局的 a;

function b(a){
    console.log(a);  // 'aaa'
    var a;  // var a是定义用的, 不赋值不会改变原有值;
    console.log(a); // 'aaa'
    console.log(window.a);  // f a(){   }
}

b("aaa");
```


### 赋值次序
* 先到后: 传的参数->变量提升->运行时赋值;
* `var a`,这步操作只会声明一个变量, 不会影响值,(已经有了 a 变量, 就不处理);
```
运行时复制生效
function b(a){
    a = "hello";  //最后运行的时候赋值;
    console.log(a);  // 'hello'
    function a(){};
    console.log(a);  // 'hello'
}

b("aaa")
```
```
变量提升赋值生效
function b(a){
    console.log(a);  // 'f a(){ }'
    function a(){};  // 函数声明后, a函数提升;
    console.log(a);  // 'f a(){ }'
}

b("aaa")
```
```
传的参数生效
function b(a){
    console.log(a);  // 'aaa'
    console.log(a);  // 'aaa'
}

b("aaa");
```

### call , apply , bind 区别
* `a.call(b, it1, it2, it3)`;
* `a.apply(b, [it1, it2, it3])`;
* `a.bind(b)(it1, it2, it3)`;

### 闭包
* 函数的作用域取决于声明时,而不取决于调用时

### 事件 input
* `click`: 点击;
* `focus` : 获取焦点;
* `blur` : 失去焦点;
* `keydown` : 按下按键;
* `input` :  内容改变;
* `keyup` : 松开按键;
* `select` : 选中一部分文字;
* `e.target.value`: 获取的值;

### 事件 select
* `change` : 选中项改变;
* `blur`;
* `focus`;
* `click`;
```
let ele = document.createElement("option");
ele.innerText="我是最大值";
ele.value=100;

e.target.add(ele);  // 添加一项;
e.target.remove(e.target.childNodes[0]);  // 删除第一项;
```

### addEventListener
* `元素.addEventListener(事件, 回调函数, 捕获(true)/冒泡(默认,flase))`;
```
document.getElementsByTagName("ul")[0].addEventListener("click", function(e){
    e.target;  //点击的目标元素;
    this;  // ul元素;
});
```
注: 
1. 点击事件`onClick="func"`(大写), `<input type="text" onClick="func">`;
2. 点击事件`onclick`, `onblur`等(小写);
```
document.getElementsByTagName("input")[0].onclick = function(){ };
```
3. 点击事件
```
document.getElementByTagName("input")[0].addEventListener("click", func[, 冒泡/捕获]);
```

### 属性
* 添加属性: `ele.setAttribute(属性名, 属性值)`, `ele.setAttribute(单属性名, '')`;
* 获取属性: `ele.getAttribute( 属性名 )`;
* 移除属性: `ele.removeAttribute(属性名 )`;


### 跨域
1. jsonp
```
// 定义回调函数
function func1(response){ console.log(response); }

//创建节点
var script = document.createElement("script");
// 添加节点 src=[url?] [& 属性=值]* [callback= 回调函数名 ] ;
script.src = "https://api.douban.com/v2/book/search?q=javascript&count=1"+"&callback=handleResponse";
src.type="text/javascript";
// 插入 script, 会立即生效;
document.body.insertBefore(script, document.body.firstChild);
```

2. ajax()
```
$.ajax({
    url: 'http://www.domain2.com:8080/login',
    type: 'get',
    dataType: 'jsonp',  // 请求方式为jsonp
    jsonpCallback: "onBack",    // 自定义回调函数名
    data: {},
    success: function(result){

    },
});

```


# `http://www.cnblogs.com/lzhlearn/p/5807872.html`;