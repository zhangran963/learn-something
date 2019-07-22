```js
// 解析 url字符串
let arrObj = location.search.replace('?', '')
.split('&')
.map(item => /(?<key>\w*)=(?<value>\w*)/.exec(item).groups)
.map(item => ({[item.key]: item.value}))

arrObj = Object.assign({}, ...arrObj);
```


```js
// 合成 url字符串
let keyValueArr = [];
for(let key in arrObj){
    keyValueArr.push(`${key}=${arrObj[key]}`)
}
keyValueArr.join('&')
```