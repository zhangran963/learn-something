数组内建方法:
1. Array.from()
生成数组
`Array.from({length:10}, (v,i)=> i);`
数组合并+去重
```
var a = [1,2,3];
var b = [1,2,3,4];
function conbine(){
    let arr = [].concat.apply([], arguments);
    return Array.from(new Set(arr));
}
conbine(a,b);  //[1,2,3,4]
```

2. Array.prototype.concat( 内容 );
连接多个数组
`[].concat( [1,2], [4,5,6])`, 返回新数组;

3. 转成字符串.toString()
`[1,2,3].toString()` 转换成 `"1,2,3"`;

4. Array.isArray( likeArr );
判断是否是数组
`Array.isArray( likeArr )`返回`true/false`;

5. Array.of()
生成数组;
Array.of() 方法创建一个具有可变数量参数的新数组实例，而不考虑参数的数量或类型。(更像 arr = [1,2,3])
```
Array.of(3)  //[3]
Array.of(1,2,3)  //[1,2,3]
new Array(3)  //[empty*3]
new Array(1,2,3)  //[1,2,3]
```

6. 是否都符合Array.prototype.every
`Array.prototype.every( (val, i)=>{ 判断函数 } )` 返回 `true/false`;

7. 是否有符合的 Array.prototype.some
`Array.prototype.some( (val, i)=>{ 判断函数 } )` 返回 `true/false`;

8. 迭代器Array.prototype.entries
返回类似对象的迭代器{0: item1; 1: item2 ...};
```
var a = [1,2,3];
var aobj = a.entries()
for(let i of aobj){
	console.log(i)
}
// [0, 1]
// [1, 2]
// [2, 3]
```


