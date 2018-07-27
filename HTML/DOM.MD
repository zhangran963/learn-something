### dom0 & dom2
* `dom0`级事件示例: 
1. 在 html 中绑定:
```
<input id="myButton" type="button" value="Press Me" onclick="alert('thanks');" >
```
2. 用匿名函数绑定:
```
document.getElementById("mybutton").onClick = function(){}
```
* 特点: 只能有一个, 后面的覆盖前面的;只支持冒泡不支持捕获; 用`on`开头;

* `dom2`级事件;
1. 可以绑定多个函数;
2. 不用`on`开头;
3. 即支持冒泡又支持捕获;
