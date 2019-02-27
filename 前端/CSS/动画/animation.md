### animation
* 动画, 一种简写属性;
* 按顺序显示:
    * animation-name: 动画名称, 每个名称代表一个由@keyframes定义的动画序列;
        * 多动画名称 animation-name: test1, animation4;
    * animation-duration: 动画周期时长, 默认0s, 如 1s, 800ms;
    * animation-timing-function: 定义CSS动画在每一动画周期中执行的节奏;
        * 对于关键帧动画来说, 此属性作用于一个关键帧周期(而不是整个动画周期);
        <!-- 关键词 -->
        * `ease`
        * `ease-in`
        * `ease-out`
        * `ease-in-out`
        * `linear`
        * `step-start`
        * `step-end`
        <!-- 自定义函数值 -->
        * `cubic-bezier(0.1, 0.7, 1.0, 0.1)`: 立方贝塞尔曲线
        * `steps(4, end)`: 规定时间内用 n 步跳转到终点;
        * `frames(10)`
    * animation-delay: 延时触发动画;
    * animation-iteration-count:
        * `infinite`: 无线循环;
        * `[number]`: 优先次数循环;
    * animation-direction:
        * `reverse`: 方向相反;
        * `alternate`: 路径相反;
        * `alternate-reverse`: 方向-路径 相反;
    * animation-fill-mode:
        * `none`: 返回首帧;
        * `forwards`: 保持尾帧;
        * `backwards`: 返回首帧;
        * `both`;



* `animation: move 4s cubic-bezier(0.5,0.9,0.5,0.1) 0s infinite alternate;`
> 动画:name duration 动画方式 delay 次数 是否重复;   
初始状态(同animation同级)相当于animation的0%；  
cubic-bezier(x1,y1,x2,y2) 相当于定义开始和结束的斜率
动画方式：ease ease-in ease-out ease-in-out linear cubic-bezier(x1,y1,x2,y2);  
animation-name\ animation-duration\ animation-timing-function\ animation-delay\ animation-iteration-count\ animation-direction

* `animation-fill-mode : none | forwards | backwards | both;`动画完成后的状态;
    * none: 不改变默认行为;
    * forwards: 动画完成后, 保持最后一个状态;
    * backwards: 动画完成后, 保持开始的属性值;