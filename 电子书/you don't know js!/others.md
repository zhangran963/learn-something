### 属性描述符
查看
```
var myObj = { a: 2};
Object.getOwnPropertyDescriptor( myObj, "a");
打印出属性值
    configurable:true
    enumerable:true
    value:2
    writable:true
```
修改
```
Object.defineProperty(myObj, "a", {value:1111, enumerable: false})
```

### getter, setter
```
var myObj = {
    id: "66166",
    get a(){
        return this.id+2;
    }
}
myObj.a  //  661662
```
```
var myObj = {
    id: "66166",
    get a(){
        return this._a_+30;
    },
    set a(val){
        this._a_ = val*2;
    }
}
myObj.a = 100; //  设置setter;
myObj.a;  //  读取getter, 230, 其中myObj._a_是200;
```

### 判断某属性是否在对象中
1. `"x" in myObj` 返回true/false;
2. myObj.hasOwnProperty("x") 返回true/false;

### 继承
* `var thisObj = Object.create(myObj);` thisObj继承自myObj;
* 每个原型链都终结在`Object.prototype`;

### .valueOf()
获取数值层面的信息;
```
var myBoo = new Boolean(true); // Object类型;
var thisBoo = true;  //  Boolean类型;
// 以下等式成立:
myBoo==thisBoo;
myBoo!==thisBoo;
myBoo.valueOf()===thisBoo;
```


### localStorage sessionStorage cookies
不同浏览器无法共享localStorage或sessionStorage中的信息。相同浏览器的不同页面间可以共享相同的 localStorage（页面属于相同域名和端口），但是不同页面或标签页间无法共享sessionStorage的信息。这里需要注意的是，页面及标 签页仅指顶级窗口，如果一个标签页包含多个iframe标签且他们属于同源页面，那么他们之间是可以共享sessionStorage的。

localStorage: 
* 同源 localStorage 可以共享;
* 存储时间不受限制;

sessionStorage:
* 同源同页面(标签页) sessionStorage 可以共享;
* 仅限页面打开时可以用, 关闭后清除;
