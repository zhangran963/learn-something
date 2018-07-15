
### 属性选择器
* `a[href*="example"]`选择"href"包含"example"的元素;
* `a[href$=".org"]`选择以".org"结尾的元素;
* `a[href^="www"]`选择以"www"开头的元素;
* `a[href~="qpmall"]`选择值列表包含"qpmall"的元素,如`<input href="qianpinmao qp qpmall">`;

### 兄弟选择器
* `input+input`选择input元素后面的**相邻的**input元素, 只选中兄弟元素, *相邻* *兄弟* *后面*;
* `input~input`选择input元素后面的**不必相邻的**input元素, *不必相邻* *兄弟* *后面*; 

### 去掉 input type="number" 的上下箭头
```
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button{
    -webkit-appearance: none !important;
}
```

### 整个页面
body会随元素的而变, :root不会
```
:root{
    background-color: lightgray;
}
```

```
box-shadow:(inset) x偏移 y偏移 四周阴影 四周扩大 颜色;
```
