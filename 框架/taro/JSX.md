* 给结构赋值
```
<View data-i={1 + this.calc1()}></View>
```

* 不能使用解构模式`...`(react 中可以);
```
/* 小程序中不能这样用 */
<Greeting {...props} />  
```

* 没有给属性传值, 默认为 true;
```
<MyTextBox autocomplete />
<MyTextBox autocomplete={true} />
```

* 数据 / 方法 / 属性 
```
/* 数据值 */
<View>{name}</View>

/* 方法 */
<View>{this.calc1()}</View>

/* 属性, 好像不能用, 暂时放到数据中 */
```

* 
```

```

* 
```

```

* 
```

```

* 
```

```