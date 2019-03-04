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


### 取消重复的请求
* 保持保留最新的请求
```js
import axios from "axios";

let pending = []; // [{标识, 取消函数}, ...]
let cancelToken = axios.CancelToken;
let removePending = (config) => {
	for (let p in pending) {
		if (pending[p].u === config.url + '&' + config.method) { // 查看是否有相同的标识
			pending[p].f(); // 取消请求
			pending.splice(p, 1); // 移除记录
		}
	}
}

axios.interceptors.request.use(config => {
	removePending(config); //如果记录中有相同标识的请求, 取消掉旧的, 用本次请求
	config.cancelToken = new cancelToken((c) => {
		// u:本次请求的标识; f:本次请求的取消函数
		pending.push({ u: (config.url + '&' + config.method), f: c });
	});

	return config;
}, Promise.reject);


axios.interceptors.response.use(response => {
	removePending(response.config);  //在一个ajax响应后再执行一下取消操作，把已经完成的请求从pending中移除

    return response
}, Promise.reject)
```