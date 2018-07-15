**Map**是一组键值对的结构，具有极快的查找速度。
> 设置 var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
注：逗号，不是分号；

1. m.get("xxx");
2. m.set("xxx",89);
3. m.has("xxx");
4. m.delete("xxx");

**Set** 和Map类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key。
> var s = new Set(); `var s2 = new Set([1,2,3])`
1. s.add(4);
2. s.delete(3);

**for循环遍历**

`for(var value of aaa){}  `
其中{Array & set中，value是值} {Map中，value是值对，value[0]是键，value[1]是值}；
```
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    alert(element);
});
```

**arguments**   
关键字arguments，它只在函数内部起作用，并且永远指向当前函数的调用者传入的所有参数。arguments类似Array但它不是一个Array：
```
function abs() {
    if (arguments.length === 0) {
        return 0;
    }
    var x = arguments[0];
    return x >= 0 ? x : -x;
}
abs(); // 0
abs(10); // 10
abs(-9); // 9
```

每次调用filter、map、reduce等函数时，都会赋值(value,index,array)到函数，都会被arguments接收(可能没有变量接收);

**rest参数**

rest参数只能写在最后，前面用...标识，从运行结果可知，传入的参数先绑定a、b，多余的参数以数组形式交给变量rest
```
function foo(a, b, ...rest) {
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
}
foo(1, 2, 3, 4, 5);
// 结果:
// a = 1
// b = 2
// Array [ 3, 4, 5 ]
```

**let**  
申明一个块级作用域的变量：变量不提升
```
function foo() {
    var sum = 0;
    for (let i=0; i<100; i++) {
        sum += i;
    }
    i += 1; // SyntaxError
}
```
在for中用let，let的值只对for中生效，若是var，则在这个局部作用域中都生效；


要计算'x的y'次方可以用Math.pow(x, y)

number、string、boolean、function和undefined有别于其他类型。特别注意null的类型是object，Array的类型也是object，如果我们用typeof将无法区分出null、Array和通常意义上的object——{}。
> typeof
1. undefined
2. number (NaN)
3. string
4. boolean
5. function
6. object ({ },array,null)

判断Array要使用Array.isArray(arr)；

判断某个全局变量是否存在用typeof window.myVar === 'undefined'；

reg.exec("string")
> 返回null 或 [匹配值[,$1][,$2],...] 属性：index 输入：input

获取地址 及 其他方法；
> `location.href`
1. location.protocol; // 'http'
2. location.host; // 'www.example.com'
3. location.port; // '8080'
4. location.pathname; // '/path/index.html'
5. location.search; // '?a=1&b=2'
6. location.hash; // 'TOP'

加载页面
> location.assign() 加载新页面； location.reload() 刷新；

重置title
> document.title = "xxx";

返回 和 下一页(不推荐)
1. `history.back();` `history.go(-1);`
2. `history.forward();` `history.go(1);`



1. .innerHTML：充入的文字以HTML方式解析;
2. .innerText, .textContent:充入的文字就是文字，即使有"<p></p>"之类的以文本对待；

删除节点
> `self.parentElement.removeChild(self);`

<!-- 选择节点 -->
<!-- > `parent.children[1];` -->

表单的输入
> .value :对text、password、hidden、select类型
.checked :对checkbox、radio类型

<!-- 验证是否是字符串结尾 -->
<!-- >  `str.endsWith(string[,position]);` -->

读取到文件对象
> `<input type="file" enctype="multipart/form-data" method="post" id="file">`  
fileInput.files[0] :重点是 .files[0] ,然后再用".name" ".type"等读取属性；
1. 读取对象：`var reader = new FileReader();`
2. 监听对象变化：`reader.onload = function(e){
    //e.target 指reader对象，有多个属性，如result
};`
3. 开始读取 `reader.readAsDataURL( fileID.files[0] );`

**Promise**
> `var pro = new promise(function(fun1,fun2){
    <!-- fun1用在then里，fun2用在catch里 -->
})`
`pro.then(function(){ func1内容 }).catch(function(){ fun2内容 })`

并行
> `Promise.all([p1,p2,...]).then()` 同时执行p1和p2，并在它们都完成后执行then:

“或”行
> `Promise.race([p1,p2,...]).then();` 同时做p1和p2,用先返回的结果;

**canvas**  
画圆(右侧开始，终点：顺时针，填充：逆时针)
1. `ctx.clearRect(x,y,width,height)` 擦除(x,y)坐标处，宽高为width和height的区域;
2. `ctx.fillStyle = "#fff";` 设置颜色
3. `ctx.fillRect(x,y,width,height);` 把(x,y)位置处大小为width*height的矩形涂色
4. `ctx.stroke() ctx.stroke(xxx)` 绘制描好的路径 或 绘制xxx
5. `path = new Path2D()` 创建path,绘制复杂的路径
6. `ctx.arc(x,y,r,s-arg,e-arg,shun/ni);` 画圆，最后一项是顺时针(false)or逆时针(true)。
7. `ctx.strokeStyle = "#fff";` 填充的颜色

绘制文本
1. `ctx.fillText("带阴影的文字",x,y);`
2. `ctx.shadowOffsetX = number` `ctx.shadowOffsetY = number` 阴影沿X轴和Y轴的偏移;
3. `ctx.shadowBlur = number;` 阴影的模糊效果;
4. `ctx.shadowColor = "xxx";` 阴影的颜色;
5. `ctx.font = "24px 'microsoft yahei'"` 设置字体;
6. `ctx.fillStyle = "#fff";` 设置字体颜色;


### Canvas绘图模糊问题
> 大部分设备 实际像素/逻辑像素=2; 通过`window.devicePixelRadio`查看; 设备实际是2px(物理) 显示 1px(逻辑);
> canvas 的 CSS 宽高: 描述 canvas 元素的实际宽高;
> canvas 的上下文宽高(元素上直接描述的,没有'px'标识): 里面显示内容相对位置的参考;

> canvas 绘图时，会从两个物理像素的中间位置开始绘制并向两边扩散 0.5 个物理像素。当设备像素比为 1 时，一个 1px 的线条实际上占据了两个物理像素（每个像素实际上只占一半），由于不存在 0.5 个像素，所以这两个像素本来不应该被绘制的部分也被绘制了，于是 1 物理像素的线条变成了 2 物理像素，视觉上就造成了模糊;

* 解决方案示例
```
** css **
// devicePixelRatio = 2
<style>
canvas {
    width: 200px;
    height: 200px;
}
</style>

** js **
<canvas id="canvas" width="400" height="400"></canvas>

** js **
ctx.scale(2, 2);  // 放大2倍
ctx.strokeStyle = '#000';
ctx.lineWidth = 1;
ctx.strokeRect(10, 10, 100, 100);
```
