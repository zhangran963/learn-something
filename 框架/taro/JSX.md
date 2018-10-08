* 给结构赋值
```jsx
<View data-i={1 + this.calc1()}></View>
```

* 不能使用解构模式`...`(react 中可以);
```jsx
/* 小程序中不能这样用 */
<Greeting {...props} />  
```

* 没有给属性传值, 默认为 true;
```jsx
<MyTextBox autocomplete />
<MyTextBox autocomplete={true} />
```

* 数据 / 方法 / 属性 
```jsx
/* 数据值 */
<View>{name}</View>

/* 方法 */
<View>{this.calc1()}</View>

/* 属性, 好像不能用, 暂时放到数据中 */
```

* 行内样式
```jsx
<View className="header" style={{
    /* 驼峰式键值 */
    /* 使用 this */
    paddingTop: this.state.statusBarHeight+'px',
    backgroundColor: this.props.isColor?'red':'green'
}}></View>
```

### 动态 className 
```jsx
<p className={["default-class", true==1?"yes":"no"]}></p>
```


* 列表
* 最好添加`key={index}`
* 得写到 render 里面;
* return 里的js逻辑不能复杂(React 支持复杂, Taro不支持);
```js
render(){
    const content = this.state.items.map((item,i) => {
        return (
            <View className={i%2===0?'even':'odd'} key={i}>{item}</View>
        )
    });

    return (
        <View onClick={this.testFunc.bind(this)}>
            <View>
                {content}
            </View>
        </View>
    )
}
```



* 
```

```

* 
```

```