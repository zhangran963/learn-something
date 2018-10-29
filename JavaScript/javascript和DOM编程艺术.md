element.childNodes[0].nodeValue 等价于
element.firstChild.nodeValue

element.childNodes[element.childNodes.length-1]等价于
element.lastChild;

检测浏览器是否支持xxx；
> if(! xxxx) return false;

onload绑定多个函数的方法：创建一个新函数，此函数功能是1.没有onload时，加上传入的onload，有onload事件后，在onload事件后再加入新的事件；
```js
function addLoadEvent(func){
    var oldonload = window.onload;
    if(typeof window.onload != "function"){
        window.onload = func;
    }
    else{
        window.onload = function(){
                oldonload();
                func();
        };
    }
}
function firstFunction(){
    alert("第一项内容");
}
function secondFunction(){
    alert("第二项内容");
}
addLoadEvent(firstFunction);
addLoadEvent(secondFunction);
```

element.nodeName 指TagName，如 IMG 、 UL ；

文本节点的 .nodeType 的值是 3；

.onkeypress键盘按下事件，同.onclick;
> 按键赋值可以用 element.onclick = element.onkeypress ;


创建节点、文本、属性 等；插入节点；
```js
document.createElement();
document.createTextNode();
element.setAttribute(" "," ");
parent.appendChild(child);
```


在 某元素之前 插入 新元素；
> parent.insertBefore(newElement,targetElement);

没有 insertAfter() 方法, 需要自定义；
```js
function insertAfter(newElement,targetElement){
    var parent = targetElement.parentNode;
    if(parent.lastChild == targetElement){
    parent.appendChild(newElement);
    }
    else{
        parent.insertBefore(newElement,targetElement.nextSibling);
    }
}
```


画圆角矩形的函数
```js
function creatRoundRect(ctx, x1, y1, width, height, radius){
       // 移动到左上角的开始点
       ctx.moveTo(x1 + radius, y1);
       // 添加一条连接开始点到右上角的线段
       ctx.lineTo(x1 + width - radius, y1);
       // 添加右上角的一段圆弧
       ctx.arcTo(x1 + width, y1, x1 + width, y1 + radius, radius);
       // 添加一条连接到右下角的线段
       ctx.lineTo(x1 + width, y1 + height - radius);
       // 添加右下角的一段圆弧
       ctx.arcTo(x1 + width, y1 + height, x1 + width - radius, y1 + height, radius);
       // 添加一条由右下角连接到左下角的线段
       ctx.lineTo(x1 + radius, y1 + height);
       // 添加左下的圆弧
       ctx.arcTo(x1, y1 + height, x1, y1 + height - radius,radius);
       // 添加一条由左下角连接到左上角的线段
       ctx.lineTo(x1, y1 + radius);
       // 添加一段圆弧
       ctx.arcTo(x1, y1, x1 + radius, y1, radius);
       ctx.closePath();
   }
```


转到父元素
> .parentNode

function 后，有没有括号的区别
> 在为 onreadystatechange 指定函数引用时，不要在函数名后加括号；
加括号：立即引用，相当于把值引用；
不加括号：把函数引用；

abrr 缩略语

for 循环方式
```js
for(x in arr){
    全部循环，x指下标；arr指数组；
    例如：
    alert(`值是 ${myArr1[a]},下脚标号是${a}`);
}
```

accesskey 属性吧一个元素与键盘上的某个快捷键关联起来；

setTimeout(func,interval)   设置固定时间后执行；

elem.style.xxxxxx   得到的是字符串，需要 parseInt() 处理;

显示缩略图
```js
parent: {
    position:relative; 为了使img的内容嫩定位；
}
```


canvas 知识点
```js
var ctx = canvas.getContext("2d");
ctx.drawImage(img,x,y,width,height);
```
 

属性 elem.videoWidth 和 elem.videoHeight 指 视频的高度和宽度；  
属性 elem.width 和 elem.height 指 播放窗口的高度和宽度；


window.location.href 获取页面地址
