
transition: 过渡, 是一种简写属性;

按顺序显示:
* transition-property: 过渡属性的名称, 如 width, opacity;
* transition-duration: 过渡的时间, 如2s, 120ms;
* transition-timing-function: 动画的过程函数:
    * linear
    * ease
    * ease-in
    * ease-out
    * ease-in-out
    * step-start
    * step-end
    * steps(4, end)
    * cubic-bezier( x1, y1, x2, y2 )
    * ...
* transition-delay: 过渡开始的延时时间, 如2s, 4ms;



animation: 动画, 是一种简写属性;
按顺序显示:
* animation-name: 动画名称, 每个名称代表一个由@keyframes定义的动画序列;
    * 多动画名称 animation-name: test1, animation4;
* animation-duration: 动画周期时长, 默认0s, 如 1s, 800ms;
* animation-timing-function: 定义CSS动画在每一动画周期中执行的节奏;
    * 对于关键帧动画来说, 此属性作用于一个关键帧周期(而不是整个动画周期);
* animation-delay:
* animation-iteration-count:
* animation-direction:
* animation-fill-mode: