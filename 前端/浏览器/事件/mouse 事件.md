

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9uss6xufej31k00rsafp.jpg)

### 移入`mouseover` & 移出`mouseout`
* 绑定在父元素, 子元素"可继承"
  * 移入时, 父元素移入 > 父元素移出 > 子元素移入
  * 移出时, 子元素移出 > 父元素移入 > 父元素移出
* 优先触发

### 进入`mouseenter` & 离开`mouseleave`
* 仅绑定在父元素
  * 进入时, 在 mouseover 之后触发
  * 离开时, 在 mouseout 之后触发
* jQuery 的 hover() 使用的就是 mouseenter/mouseleave

### 移动`mousemove`
* 移动时触发