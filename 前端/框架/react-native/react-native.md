> 载入项
1. `AppRegistry, Text, View, StyleSheet, Image, TextInput`

> 布局
```
const css = StyleSheet.create({
  titleCSS:{   }
});
```

> 宽高比-> 宽/高 = aspectRatio

> 背景图 <ImageBackground>
需要指定宽高(不指定报错)
```
<ImageBackground source={...} style={xxx}>
    <Text>Inside</Text>
</ImageBackground>
```

TextInput组件  
详细参考地址`http://www.hangge.com/blog/cache/detail_1526.html`
> 1. `onChangeText` 在文本变化的时候会调用;
2. `onSubmitEditing` 在文本提交时调用;
3. `onFocus` 获取焦点
4. `autoFocus={true}` 自动获取焦点;
5. `multiline={true}` 支持多行文本;
6. `numberOfLines={3}` 填入内容的行数(不足行数时,自动加长;多余指定行数时,内部滑动);
7. `editable={false}` 不能编辑+字体变灰
8. `keyboardType="numeric"` 键盘弹出时的默认类型 `default; numeric:数字; email-address: 英文`
9. `underlineColorAndroid='transparent'` 去掉安卓版输入框的下划线;

FlatList组件
> 1. `keyExtractor={(item,index)=>index}` 指定用index作为键值();


本地存储AsyncStorage
> 存储
```
AsyncStorage.setItem(名字, JSON.stringify(数据), (err)=>{

})
```
> 读取
```
AsyncStorage.getItem(名字, (err, result)=>{
    if(!err){
        // 得到数据
    }
})
```
> 删除
AsyncStorage.removeItem(名字,(err)=>{
    if(!err){
        // 删除成功
    }
})


### TouchableNativeFeedback等效果反馈类
* 布局时可以忽略它们, 仅有事件类可以用;

### flatList 的内容器样式
* `contentContainerStyle={styles.flatList}`;

