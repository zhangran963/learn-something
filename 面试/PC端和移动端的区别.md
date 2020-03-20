### PC端和移动端的区别

|     |PC端|移动端||
|:--:|:--:|:--:|:--:|
|界面布局|显示内容多, 灵活布局|单列 或 响应式|
|使用习惯|适配鼠标操作, 按钮/链接等可以小一点|按钮/链接等, 至少保证手指能准确操作|
|网络速度|几乎不考虑流量/网速等|一般用移动网络, 减少大图片, 大文件等, 注重首屏加载|
|技术层面|(类似)|  有些专用的库 jQuery for mobile  |
|特殊表现||  1px变粗; 300ms延时; |
|专项测试||  响应时间/屏幕适配/弱网/流量/耗电量/其他事件打断(电话/短信/消息)/横竖屏/手势  |
||||

***

## 1px

``` scss
.border-1px {
    position: relative;

    &::after{
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 200%;
        height: 200%;
        border: 1px solid black;
        border-radius: 16px;
        transform-origin: 0 0;
        transform: scale(0.33);
    }
}
```

***

## 300ms延时

