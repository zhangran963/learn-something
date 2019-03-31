### 服务器
```js
const http = require('http');

const server = http.createServer();
server.on('request', function(req,res){
    // req.socket.remoteAddress  // 客户端IP地址
    // req.socket.remotePort  //客户端端口号
    // res.setHeader('Content-Type', 'text/plain; charset=utf-8') // 设置头部请求为普通文本类型, utf8编码
    // res.setHeader('Content-Type', 'text/html; charset=utf-8') // 设置头部请求为html类型, utf8编码
    // res.setHeader('Content-Type', 'text/jpeg')  // .jpg格式的图片, 具体对应关系, 查看http://tool.oschina.net/commons
    // res.write('内容')  // 给res添加内容,但不会响应res;
    res.end( JSON.stringify([1,2,3]) );  // 给 res添加内容并响应;
})
server.listen(7001);
```
