* `str1.trim()`消除字符串两端的空格;
* `str1.trimLeft()`消除字符串左侧的空格;
* `str1.trimRight()`消除字符串右侧的空格;

### 正则表达式-分组
`"This is a string!".replace(/^(\w+)\s(\w+)/, "$2,$1")`输出为`is,This a string!`

### 进制转换
* `0x***`16进制;
* `0***` or `0o***` 8进制;


### 把16进制数字转换成10进制数字
* `255 == parseInt(0xff, 10)`


### 把10进制数字转换成16进制字符串;
`var num = 255; num.toString(16);// "fff"`