$xxx  定义变量

echo xxxxx; 输出内容；  

var_dump($flag); 读取出来数据类型；

0x 开头：16进制；
0 开头：8进制；
1.2e3 = 1200; 7.0e-3 = 0.007;

\" \' 等

> 当" "中包含变量时，变量生效；  
当' '中包含变量时，变量不生效；

Heredoc 结构形式
> $string1 = <<<GOD  
我有一只小毛驴我从来也不骑，有一天我心血来潮骑它去赶集！  
GOD;
注：最后的 GOD; 前面不能有空格；

http://localhost/
> 本地php地址

unset();
> 设置后，字符串变为null；

定义常量 define(变量,value);
```
define("GREETING","Hello world!");
echo constant("GREETING");
```  

__FILE__
> 文档位置；

__line__
> 现在所在的行数；

true和false
> 在PHP中，true显示为1；false显示为【空】；

PHP_VERSION
> PHP版本

PHP_OS
> 系统版本

defined( xxx );
> 判断 变量 是否被定义；返回true或false；

引用赋值 $c = &$a;
> $c和$a共享同一个内存数据；

$a xor $b;
> $a 异或 $b;

"string1"."string2";
> 把 字符串1 连接到 字符串2；

$a .= "string3";
> 把 $a 连接 "string3" ，再赋值给 $a;

错误控制运算符@  $conn=@mysql_connect("localhost","username"."password");
> 将@放置在一个PHP表达式之前，该表达式可能产生的任何错误信息都被忽略掉；

$num = rand(1,10);
> 取（x,y）之间的随机数；

foreach (数组 as 值){
//执行的任务
}  
foreach (数组 as 下标 => 值){
 //执行的任务
}

break; 结束**循环**；

print_r($array);
> 输出数组结构；

新字符串 = str_replace(被替换值，替换值，原字符串);

function_exists('函数名') class_exists('类名') file_exists()
> 检测函数是否存在； 检测类名是否存在；文件是否存在；

trim() ltrim() rtrim()
> 去掉两端空格，去掉左空格，去掉右空格；不改变原字符；

strlen(xxx);
> 字符串长度；1汉字=3；1数字=1字母=1；

substr(字符串变量,start,number);
> 英文字符串的截取；

mb_substr(字符串变量，start,number,网页编码);
> 给汉字用的

strpos(string, indexStr, [start]);
> 查找字符串

str_replace(目标str, 替换str, string);

sprintf('%01.2f',number);
> %:开头; f:结尾; 0:用零补齐头部； 1:最少1位(包括小数点); .2:小数点后有2位;

implode([分隔符]，数组);
> 把数组用[分隔符]连接未字符串；

explode([分隔符],$str);
> 把字符串有[分隔符]分割为数组;

addslashes();
> 给字符串加上转义字符;

preg_match("正则式", 字符串);
> 把正则式匹配字符串，返回true或false；

preg_quote(字符串，'/')
> 把原字符串转换为 正则表达式；
