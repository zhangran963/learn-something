### input元素输入内容时

``` js
changeInput(e) {
    let {
        name: key,
        value
    } = e.target;

    console.log('* 键值对: ', key, value)
    /* 注: 没有通过setState改变数据 */
}
```

* 在Taro中, 显示输入的内容; 
* 在React中, 不显示输入的内容(和实际数据表现一致); 

***

### 直接改变深层数据

``` js
changeInput(e) {
    let {
        name: key,
        value
    } = e.target;

    console.log('* e', key, value)
    let {
        user
    } = this.state /* user是深层对象 */
    user[key] = value

    /* 注: 未设置 this.setState({user}) */
}
```

* 在Taro中, 表现正常; 
* 在React中, 表现不正常; 打开setState, 表现正常; 

* 推荐, 做成如下形式:
```js
changeInput(e) {
		let { name: key, value } = e.target;

		this.setState(({ user }) => {
			user[key] = value;
			return { user };
		});
}
```
***

