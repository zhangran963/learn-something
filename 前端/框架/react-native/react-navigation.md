### 获取页面 key
* 获取此页面的 key 值: `this.props.navigation.state.key`;

### 页面导航函数
* 只有页面有, 组件没有: `const { navigate, goBack, state } = this.props.navigation`;

### 去往下一页
* `navigate('DetailPage', 数据 )`;

### 取值
* `数据 = this.props.navigation.state.params`;

### 返回
* `goBack( 返回页的 key )`; 注: 是返回页的 key 不是目标页的 key;
