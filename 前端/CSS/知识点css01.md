### 知识点


> 允许你修改CSS可视化模型的坐标空间。通过transform，可以让元素进行移动（translate）、旋转（rotate）、缩放（scale）、倾斜（skew）。   举例如下：  
transform: scale(1.4)  放大1.4倍；字体也会拉伸；

vh   vw  
> 单位，相对于视口的高度和宽度，视口被均分为100单位的vh或vw，  

:first-letter设置首字母
:first-line 设置首行


```
{
    display:flex;
    justify-content:center;
    align-items:center;                                               

    xxx{
        
    }
}
```
> **垂直** 居中弹性盒的各项div元素，需配合display:flex 使用；   
另有：  
flex-start 对齐到侧轴起点  
flex-end 对齐到侧轴终点  
baseline 与基准线对齐  
stretch  拉伸元素以适应  
inherit

针对子元素有 align-self

> **水平** 居中弹性盒的各项div元素，需配合display:flex 使用；   
另有：  
flex-start 从行首起始位置开始排列  
flex-end 从行尾位置开始排列  
space-between 均匀排列每个元素,首个元素放置于起点，末尾元素放置于终点  
space-around 均匀排列每个元素,每个元素周围分配相同的空间  
inherit


transform-origin:100%;  
> 设置旋转的基点，示例中是按右侧端点顺时针（默认）旋转  
rotate()的旋转默认在50%位置；

transform:rotate(45deg);  
> 旋转的角度；  

transform:translateY(xxx);  
> 在上下维度移动；  

transition:属性1 duration, 属性2 duration ...  
> 定义这些动作的时间段 (默认的动作都是瞬时完成)；  
需要配合1. 原始状态； 2.最终状态（写到对应的操作里，如hover）
注：一般width、color等需要2个状态，transform只需要一个状态；
***

:root  
> 伪类匹配文档树的根元素。应用到HTML，:root 即表示为<html>元素，除了优先级更高外，相当于html标签选择器。   

--xxx  自定义变量，此变量仅可用于子元素  
var(--xxx)   使用定义的变量
```
:root {
  --main-bg-color: pink;
}

body {
  background-color: var(--main-bg-color);
}
```


text-transform:uppercase   
> 用css转换为大写；  
lowercase  转换为小写；  
capitalize 首字母转换为大写；    

box-shadow:inset 0 0 10px rgba();  
> 默认(无inset)是外部阴影，有inset是内部阴影；  

2种渐变：直线、径向  
```
linear-gradient(to top,色值1 0%, 色值2 100%);
radial-gradient(circle 50px,#f00, #ff0);
```
> 渐变颜色的设置方法(方向， 色值 位置，色值 位置 ...)；  

background-size:cover;/contain
> 设置背景图片大小。cover:占满框/contain:包括全部图片;

flex-wrap:wrap;
> 指定单行显示还是多行显示（如果超出）。父元素设置flex和wrap/nowrap/wrap-reverse后，指定子元素排列方式
nowrap： 不换行;  
wrap: 换行;  
wrap-reverse: 换行 + 底左部开始排列；

font-size:0; 去掉inline-block元素之间的空格
> 在外层元素上设置font-size：0；在内层元素上加上font-size：xxx；

vertical-align: text-bottom   设置在图片上，使图片与文字底部基线对齐

vertical-align: 设置在图片上，
> bottom 使图片与文字行底部对齐
middle 使图片与文字行中部对齐
top 使图片与文字行顶部对齐
text-top 使图片与文字顶部对齐  
text-bottom 使图片与文字底部对齐  
sub 使图片与文字上标对齐
super 使图片与文字下标对齐

hr 的设置方式
> <hr style=" height:2px;border:none;border-top:2px dotted #185598;" />

text-align: justify;text-align-lastjustify  实现两端对齐的方式


选择最后一个元素
> p:last-of-type{ ... };

animation: move 4s cubic-bezier(0.5,0.9,0.5,0.1) 0s infinite alternate;
> 动画:name duration 动画方式 delay 次数 是否重复;   
初始状态(同animation同级)相当于animation的0%；  
cubic-bezier(x1,y1,x2,y2) 相当于定义开始和结束的斜率
动画方式：ease ease-in ease-out ease-in-out linear cubic-bezier(x1,y1,x2,y2);  
animation-name\ animation-duration\ animation-timing-function\ animation-delay\ animation-iteration-count\ animation-direction

* `animation-fill-mode : none | forwards | backwards | both;`动画完成后的状态;
    * none: 不改变默认行为;
    * forwards: 动画完成后, 保持最后一个状态;
    * backwards: 动画完成后, 保持开始的属性值;


### 隐藏滚动条并可以滑动内容
```
# html和body元素
html {
    overflow: -moz-hidden-unscrollable;
    height: 100%;
}

body::-webkit-scrollbar {
    display: none;
}

body {
    -ms-overflow-style: none;
    height: 100%;
	width: calc(100vw + 18px);
	overflow: auto;
}
# 子元素
body的子元素 div, section, header等,设置宽度 width:100vh;
```
