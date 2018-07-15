***
## 引入示例
***

### ES6语法
```
/* child */
export function func1(){
    console.log("我是 func1");
}

/* parent */
import { func1 } from "./child.js";

// 引入的函数就行在本页定义的一样;
func1();
```

### exports & require 语法
``` 
/* child */
exports.square = function(x){
    return x*x;
}
exports.cube = function(x){
    return x*x*x;
}

/* parent */
let math = require("./math);
// 使用
math.square(x); 
math.cube(x);
```

### module.exports & require 语法
```
/* child */
function square(x){ return x*x; }
function cube(x){ return x*x*x; }
module.exports = {
    square: square,
    cube: cube
}

/* parent */
let math = require("./math");

// 使用
math.square(x);
math.cube(x);
```


### require 和 import
```
let math = require("./math");
等效于
import math from require("./math");


let { square, cube } = require("./main");
等效于
import { square, cube } from "./math";
```