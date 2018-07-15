### for 循环
```
/* js */
data: {
    myList: [{name: '张三'}, {name: '李四'}],
}

/* wxml */
<view wx:for="{{myList}}">
    <text>{{item.name}}</text>
</view>
```


### if
```
/* js */
data: {
    id: 171,
}

/* wxml */
<view>
    <text wx:if="{{id==170}}">我是组长</text>
    <text wx:elif="{{id==171}}">我是副组长</text>
    <text wx:else>我是组员</text>
</view>
```

### if 和 hidden
* `if`按需求渲染, 适用变化不频繁的场景;
* `hidden`总会渲染,只是有显示不显示的区别, 适合频繁变化的场景;

### <block>标签
* 是一个包装元素, 在页面中不会渲染元素, 只接受控制属性;


### template模板
* 渲染的模板;
* `<template>`这个元素不渲染;

```
/* 引入模板 */
<template is="msgItem" data="{{...msgItem}}"></template> 

/* 设置模板 */
<template name="msgItem">
	<view>
		<text>{{index}}: {{msg}}</text>
	</view>
</template>
```
* 根据条件渲染
```
/* template模板 */
<template name="odd">
  <view> odd </view>
</template>
<template name="even">
  <view> even </view>
</template>

<block wx:for="{{[1, 2, 3, 4, 5]}}">
    <template is="{{item % 2 == 0 ? 'even' : 'odd'}}"/>
</block>
```
* 渲染对象数据
```
/* js */
data: {
    msgItem: {
        index: 101,
        msg: "这是一条消息",
        time: "2017-12-26"
    }
}

/* template */
<template name="msgItem">
	<view>
		<text>{{index}}: {{msg}}</text>
		<text>
			{{time}}
		</text>
	</view>
</template>
```

### template 导出/引入
* 只能 import目标文件定义的模板, 不能 import目标文件 import的模板;
```
/* logs.wxml 导出 */
<template name="xianshi">
	<text>这是显示框 {{name}}</text>
</template>

/* index.wxml 引入+使用 */
<import src="../logs/logs" />
<template is="xianshi" data="{{...msgItem}}"></template>
```

### include
* include 可以将目标文件除了 <template/> <wxs/> 外的整个代码引入，相当于是拷贝到 include 位置;
```
<!-- index.wxml -->
<include src="header.wxml"/>
<view> body </view>
<include src="footer.wxml"/>

<!-- header.wxml -->
<view> header </view>

<!-- footer.wxml -->
<view> footer </view>
```


### 事件
1. `bindtap="func1"`或`bind:tap="func1"`形式, 冒泡;
2. `catchtap="func1"`或`catch:tap="func1"`形式, 不冒泡;
    * `touchstart`: 触摸开始;
    * `touchend`: 触摸结束;
    * `touchmove`: 触摸并移动;
    * `touchcancel`: 触摸被中断,如电话/弹窗等;

    * `tap`: 点击;
    * `longpress`: 长按;

* 其他常用事件都是非冒泡事件, 如`input`,`submit`等;


### 捕获事件
* `capture-bind`(向下冒泡),`capture-catch`(不向下冒泡)


### scroll-view
* 竖向滚动, 需要设置 `scroll-y`;
* css设置scroll-view的高度;
* `scroll-top=数字`竖向滚动条的初始位置;
* `upper-threshold=数字`距离顶部/左部多远时,触发scrolltoupper事件;
* `lower-threshold=数字`距离底部/右侧多远时,触发scrolltolower事件;
* `scroll-into-view=字符串(id名)`滚动到指定 ID名 的元素处;
* `enable-back-to-top`iOS点击顶部状态栏、安卓双击标题栏时，滚动条返回顶部，只支持竖向;
* `bindscrolltoupper=字符串(函数名)`滚动到顶部/左部, 触发函数;
* `bindscrolltolower=字符串(函数名)`滚动到底部/右部, 触发函数;
* `bindscroll=字符串(函数名)`滚动时, 触发函数;
```
/* wxml */
<scroll-view scroll-y="{{true}}">
	<view class='box'>
		卓一航
	</view>
	<view class='box'>
		卓一航
	</view>
	<view class='box'>
		卓一航
	</view>
	<view class='box'>
		卓一航
	</view>
</scroll-view>
```

* 横向滚动, 需设置 `scroll-x`;
* css 设置 scroll-view 的宽度;
* `scroll-left=数字`横向滚动条的初始位置;
```
/* wxml */
<scroll-view scroll-y="{{true}}">
	// 里面的内容比较宽, 会出现滚动条;
</scroll-view>
```

### icon
* `type:string` 设置的值: `success/ success_no_circle/ info/ warn/ waiting/ cancel/ download/ search/ clear` ;
* `size:number` 设置大小;
* `color:string` 设置颜色;
* 示例: `<icon type="success" size="23" color="green"></icon>`;

### text
* `selectable:boolean` 文本是否可选择;
* `space:string` 设置空格样式: `ensp:中文的一半` `emsp: 和中文宽度一样` `nbsp: 根据字体设置的空格大小`;
* `decode:boolean` 是否解码: 是否把`&nbsp; &lt; &gt; &amp; &apos; &ensp; &emsp;`解码成代表的内容;

### rich-text
* 能够把 html中的 div/code/h2/label/span 等标签用富文本的形式展示;
* 富文本的代表含义定义在数据中;

1. 元素节点: `type=node`
* `name:string` 标签名;
* `attrs:object` 属性;
* `childred:array` 子节点列表;

2. 文本节点: `type=text`
* `text:string` 文本;

```
<!-- rich-text.wxml -->
<rich-text nodes="{{nodes}}" bindtap="tap"></rich-text>

// rich-text.js
Page({
    data: {
        nodes: [{
        name: 'div',
        attrs: {
            class: 'div_class',
            style: 'line-height: 60px; color: red;'
        },
        children: [{
            type: 'text',
            text: 'Hello&nbsp;World!'
        }]
        }]
    },
    tap() {
        console.log('tap')
    }
})
```

### progress
* 进度条
* 需要配合 css, 否则看不见条, 如`width: 750rpx; height: auto;`;
* `percent="20"`: 设置显示的进度是20%;
* `show-info`或`show-info="{{true}}"`: 设置右侧显示`20%`字样;
* `stroke-width="3"`: 设置进度条宽度是`3rpx`;
* `activeColor="red"`: 设置进度条(已选择部分)颜色;
* `backgroundColor="gray"`: 设置进度条背景色(未选择部分)颜色;
* `active`: 设置进度条从左往右的动画;
* `active-mode`: 动画形式: 字符串;
    * `backwards`: 从头播;
    * `forwards`: 从上次结束点开始播;


### button
* 按钮, 背景灰色, 黑色字;
* `size="mini"`: `default`/`mini`;
* `type="default"`: `primary`(绿色)/ `default`(黑色)/ `warn`(红色);
* `form-type="submit"`: `submit`提交表单/ `reset`重置表单;
* `plain`: 按钮是否镂空(背景色透明);
* `disabled`: 是否禁用;
* `loading`: 文字前带有加载中动画;
* ``


### navigator导航元素
* 类似 a标签 ;
* `url="../detail/detail"`做页面跳转;
* `open-type=字符串`: 跳转方式;
    * `navigate`: 普通跳转;
    * `redirect`: 重定向, 对应`wx.redirectTo`;
    * `switchTab`;
    * `reLaunch`;
    * `navigateBack`;


### image
* `src=字符串(路径)`: 路径;
* `mode=字符串`: 裁剪或缩放模式;
    * `scaleToFill`改变宽高比使适应 image 元素宽高;
    * `aspectFit`宽高比不变+全部显示(有空白);类似`background-size: contain`;
    * `aspectFill`宽高比不变+全部占满;类似`background-size: cover`;
    * `widthFill`宽高比不变+高度自适应(设置的 css高度 没用);
    * `top`.`bottom`.`center`.`left`.`right`.`top left`.`top right`.`bottom left`.`bottom right`宽高比不变+大小不变,裁剪适当位置;


### picker 选择器
* `mode='selector'`普通选择器(默认);
    * `range=数组`: 数据;
    * `range-key=字符串`: 当数据是 object[] 形式时,指定显示内容是 object 的哪一个属性;
    * `value=索引`: 选择器展开时,选中的是哪一项;
    * `bind:change=函数`: 选中值改变时的回调函数;
    * `disabled`: 是否禁用;
    * `bind:cancel=函数`:遮罩层收起时(取消),触发的回调函数;

* `mode='multiSelector'`多列选择器;
    * `range=(二维)数组`: 数组中存放多列内容,每一列内容同普通选择器;
    * `range-key=字符串`: 二维object[] 里要显示的属性;
    * `value=数组`: 多列选择器的选中值;
    * `bind:change=函数`: 选中值改变时的触发函数;
    * `bind:columnchange=函数`: 某一列值改变时触发;
    * `bind:cancel=函数`: 弹窗取消时触发;
    * `disabled`: 禁用;

* `mode='time'`: 时间选择器;
    * `value=字符串`: 默认选中的时间, eg: `09:30`;
    * `start=字符串`: 开始时间, eg: `08:00`;
    * `end=字符串`: 结束时间, eg: `21:45`;
    * `bind:change=函数`: 选中时间改变后的回调函数;
    * `disabled`: 禁用;

* `mode='date'`: 日期选择器;
    * `value=字符串`: 默认选择日期, eg: `2017-04-23`;
    * `start=字符串`: 最早日期: eg: `2015-09-21`;
    * `end=字符串`: 最晚日期: eg: `2018-10-31`;
    * `fields=字符串`: 显示的最小单位: `day`(默认)/`month`月份/`year`年份;
    * `bind:change=函数`: 选中值改变时, 触发项;
    * `bind:cancel=函数`;
    * `disabled`: 禁用;

* `mode='region'`: 省市区选择器;
    * `value=数组`: 表示选中的省市区,默认选中每一列的第一个值;
    * `custom-item=字符串`: 给每一列的头部添加一个自定义项;
    * `bind:change=函数`: 选中值改变的回调函数;
    * `disabled`: 禁用;