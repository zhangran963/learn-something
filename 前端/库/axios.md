### get请求
```js
axios.get('url地址?name1=value1&name2=value2').then('回调')

axios.get('url地址', {
    params: {
        name1: 'value1',
        name2: 'value2'
    }
}).then('回调')
```



### post请求
```js
axios.post('url地址', {
    name1: 'value1',
    name2: 'value2'
}).then('回调函数')
```