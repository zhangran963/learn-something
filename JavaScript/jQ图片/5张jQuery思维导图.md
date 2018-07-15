.attr() 读取的时候只能读取一个；需用.each()函数遍历
> $(".box").each(function(){
    console.log($(this).attr("id"));
});  
$(".box").each(function(index,element){
    console.log(index,element);
});

jQ中的each方法
```
$(xxx).each(function(index,elem){
    index:索引
    elem:此时的元素对象
});
```
```
$.each(target,function(index,elem){
    index:索引
    elem:此时的元素对象
});
```

获取元素相对于页面(文档)的位置
> $().offset(); 得到一个对象，有left 和 top 属性；

获取元素相对于有定位属性的祖辈元素的位置
> $().position(); 得到一个对象，有left 和 top 属性；

获取类型
1. typeof;  //简单
2. Object.prototype.toString.call();  //详细

event.pageX   event.pageY
> 事件发生的x坐标、事件发生的y坐标(相对于页面文档);

事件委托（点击子元素，父祖元素响应）
```
$("ul").click(function(ev){
    $(ev.target).not("li").css("background-color","red");
});
```

jQ中，事件后的function中的变量，是指事件,如上所示 ev.target 是此 item的html代码
1. 选中事件：ev.target   例:"<a href="#">tttt</a>"
2. 事件类型：ev.type    例："mouseover"
3. 事件坐标：ev.pageX  ev.pageY  例：151

事件代理语句
1. `$(ev.target).css("color","red");`
2. `ev.target.style.color = "red";`


ev.target 返回事件的目标节点（触发该事件的节点），如生成事件的元素、文档或窗口

动画
1. `$("div").animate(最终状态，执行时间，回调函数)`
2. `$(ev.target).animate({color:"red"},300);`错误！animate没有提供颜色的动画

`$("form").serialize()``$("input").serialize()` 直接序列化(生成url形式),类似userId=diyihh&password=dierhh, 其中

`$(selector).empty()` 清空


设置ajax的默认值
```
$.ajaxSetup({
    //和ajax的设置方式一样
    })
```

获取页面宽度/高度
* `document.documentElement.clientWidth`
* `document.documentElement.clientHeight` 高度有最小值

通过字符串赋值多个CSS;
* `oParent.style.cssText = "width:"+oBoxW*cols+"px;margin:0 auto";`效果同
* `oParent.style ="xxx"`;


两种形式的区别:
| window.onload | $(document).ready(xxx)|
|---------------|-----------------------|
| 全部加载完才执行 |  DOM结构加载完毕就执行   |
| 只能写一个      |   可以写多个            |
|    null       |  $(function(){  容 })  |