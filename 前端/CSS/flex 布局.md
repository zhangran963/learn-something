flex多行布局
* 重点是`flex-flow: row wrap;`和`width: 50%;`;
```html
<ul class="flexcontainer">
    <li>Something</li>
    <li>Fox Example</li>
    <li>All About Web</li>
    <li>Fox Example</li>
    <li>Something</li>
    <li>Fox Example</li>
    <li>Something</li>
    <li>Fox Example</li>
</ul>
```
```css
.flexcontainer {
    width: 300px;
    display: flex;
    flex-flow: row wrap;
}
.flexcontainer li {
    width: 50%;
    background-color: pink;
}
```

### 父元素
* `justify-content: center`: 单行横向布局格式;
    * `flex-start` .`flex-end` .`center` .`space-between` .`space-around`;
* `align-items: center`: 单行纵向布局格式;
    * `flex-start` .`flex-end` .`center` .`stretch` .`baseline`;
* `align-content: center`: 多行纵向布局格式(项数过多, 挤下去了);
    * `flex-start`: "行"往头部排, 左对齐;
    * `flex-end`: "行"往尾部排, 左对齐;
    * `center`: "行"往居中排, 左对齐;
    * `stretch`: "行"占满高度, 左对齐;
    * `space-between`: "行"两段对齐, 左对齐;
    * `space-around`: "行"平均分布对齐, 左对齐; 


### 两端对齐(多行)
```css
p{
    text-align:justify;
    text-align-last:justify;
}
```

### 两端对齐(单行)
```css
p{
    text-align:justify;
    text-align-last:justify;
    height:24px;
}
p:after{
    display:inline-block;
    content:'';
    overflow:hidden;
    width:100%;
    height:0;
}
```