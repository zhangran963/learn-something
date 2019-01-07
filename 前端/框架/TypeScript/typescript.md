`npm install -g typescript` 安装;
`tsc helloworld.ts` 编译;

### 关于视频"观看TypeScript实站"
`tsc -init` 初始化配置文件;
`tsc -w` 监听并自动编译ts文件(生成 <同名>.js);


### 错误
* 生成错误 `throw new Error('自定义内容')`;


### enum 类型
* 生成键值对称的对象
```ts
color[color["name"] = 1] = "name";
// { '1': 'name', name: 1 }
```

### readonly vs const
* 最简单判断该用readonly还是const的方法是看要把它做为变量使用还是做为一个属性。 做为变量使用的话用 const，若做为属性则使用readonly。



### 接口
* 多个类型`string|number`;
```ts
interface Person{
    name: string,
    age: number,  // 必选属性
    job?: string, //可选属性，表示不是必须的参数
    readonly salary: id,  //表示是只读的属性,但是在初始化之后不能重新赋值，否则会报错
    reset():void;   // 函数类型
    [ 名称 : string ] : 类型,  // 任意类型, 这个得类型包含前面声明的类型
}
```


### 函数类型的 interface
* 函数类型的类型检查来说，函数的参数名不需要与接口里定义的名字相匹配;
```ts
interface SearchFunc {
  (source: string, subString: string): boolean;
  // 参数1: source;  参数2: subString;
  // 返回值: boolean;
}
```


### public / private/ protected
|       |    public    |    private   |    protected   |
|-------|------|-----|------|
| 本身类   |     能   |   能     |     能     |
| 派生类   |     能   |   不能     |     能     |
| 本身   |     能   |   不能(实际能读取) | 不能(实际能读取) |


### 关闭 String 与 string 的区别
* `String` 是 JavaScript 中合法的类型; `string` 是 TypeScript 中才合法类型;
* `new String("xxx")`写成 `String` 类型; `"我是字符串"`写成 `string` 类型;
