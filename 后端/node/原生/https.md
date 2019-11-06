### https服务器
```js
const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const { default: enforceHttps } = require('koa-sslify');


// 开启 https
app.use(enforceHttps({
  port: 443
}));
// http 监听80端口, 重定向到 443 端口
http.createServer(function(request, response){
  // 重定向
}).listen(80);

// 真正的 https 服务器
https.createServer({
  // SSL options
  key: fs.readFileSync(path.resolve(__dirname, './common/ssl/key.key')),
  cert: fs.readFileSync(path.resolve(__dirname, './common/ssl/pem.pem'))
}, function(request, response){
  // 业务请求
}).listen(443);
```