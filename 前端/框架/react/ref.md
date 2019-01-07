ref: 获取 DOM 元素
> ref 属性接受一个回调函数，它在组件被加载或卸载时会立即执行。React 组件在加载时将 DOM 元素传入 ref 的回调函数，在卸载时则会传入 null。ref 回调会在componentDidMount 或 componentDidUpdate 这些生命周期回调之前执行。
* 函数式组件不能使用 ref;
```
** jsx **
return (
    <div>
        <input typ="text" ref={(input)=>{this.input = input;}} />
        // input表示 dom 元素; 和`e.target`一样;
        <input value="获取焦点" onClick={()=>{this.input.focus()}}/>
    </div>
);

或
// 这个只能用在 class 中;
componentDidMount(){
    this.textInput.focusTextInput();
}
```