等效:
* `<p firstname="四" lastname="叶草"></p>`
* `props={firstname: '四';lastname: '叶草'}; <p {...props}></p>`

### 数组形式
```
return [
    // 不要忘记 key :)
    <li key="A">First item</li>,
    <li key="B">Second item</li>,
    <li key="C">Third item</li>,
];
```