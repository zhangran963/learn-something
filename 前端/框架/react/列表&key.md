### 列表

```
** 组件 **
render(){
    let data = [1,2,3,4,5];
    
    return (
        <ul>
            {
                data.map((val,i)=>{
                    // 设置的key值在重复的元素上;
                    return <li key={i}>{val.name}: {val.age}</li>
                })
            }
        </ul>
    );
}
```