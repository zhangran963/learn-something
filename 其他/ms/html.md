### form标签属性
* action: url地址;
* method: get/post,发送表单数据的方法;
* enctype="",`application/x-www-form-urlencoded`默认值,编码所有字符, `multipart/form-data`用于一个type,属性设置为 "file", `text/plain`空格转换为 "+" 加号，但不对特殊字符编码;
* name: 表单名称;
* novalidate: 此表单内容提交时不验证;
* autocomplete="on/off": 是否启动表单的自动完成功能;


### input标签属性
* autocomplete="on/off" 是否启用浏览器的自动完成功能;
* autofocus="autofocus" 页面加载时,自动获取焦点;
* checked="checked" 页面加载时,自动选中(type="checkbox/radio");
* disabled="disabled" 禁用此元素;
* max="4" 输入数字的最大值;
* min="1" 输入数字的最小值;
* maxlength="10" 输入的最大长度(text下生效);
* name 名称;
* pattern="[0-9]" 输入的值点提交时,经过正则判断;
```
<form action="">
    <input type="text" name="name" autocomplete="off" id="input" pattern="[0-3]?" title="错误提示信息" >
    <input type="submit"> 
</form>

# input事件,每次改变value值触发(不包括js改变value时)
input.addEventListener("input",function(e){
    e.target.validity.valid;  // 是否符合验证规则
    e.target.value;  // 已经输入的值
    e.target.setCustomValidity('这是js改变的提示信息');  // 通过js改变提示信息
})

# 合法的内容样式
input, input:valid{
    
}
# 不合法的内容样式
input:invalid{
    
}
```
* title="xxxxxx" 经过pattern中的正则判断后,不通过时的提示信息;
* multiple="multiple" 上传文件时,支持多个文件;
* placeholder="xxx" 默认提示信息;
* readonly="readonly" 只读;
* required="required" 必填项;
* step="0.5" 输入合法的字符间隔;
* type="xxx" 类别`button/checkbox/file/hidden/image/password/radio/reset/submit/text`;


### box-sizing属性
使用W3C标准盒模型, 需要在HTML头部加上`<!doctype html public "-//w3c//dtd xhtml 1.0 transitional//en" "http://www.w3.org/tr/xhtml1/dtd/xhtml1-transitional.dtd">`
1. `content-box`(默认) 标准盒模型,宽度高度指content;
2. `border-box` IE盒模型,宽度高度指border;


### position属性
1. relative
相对原位置移动,占原位置;
2. absolute
相对上一个定位元素,不占原位置;
3. fixed
相对浏览器窗口,不占原位置;
4. static(默认)
没有定位信息;
5. sticky(static+fixed);
在父元素中>自定义设置(left/top/right/bottom)>流中(正常)  
在流中
