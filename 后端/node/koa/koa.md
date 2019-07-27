### 启动
`node xxx.js`

### 引入
* 引入 koa, 开启简单服务;
```js
const Koa = require('koa');
const app = new Koa();

app.use(async (ctx, next) => {
    // ctx.request.socket.remoteAddress 客户端ip地址
    // ctx.request.socket.remotePort  端口号
    // ctx.request.socket.remoteFamily  例'IPv6'
    ctx.response.body = "没有你以后, 一个人四处旅游, 以后的以后, 我钱着别人衣袖, 若是有缘再见, 也会笑着问候";
});

app.listen(3000);
```
* ``
* `ctx.request.url`: 域名后面的路径, 同`ctx.request.originalUrl`;
* `decodeURIComponent(ctx.request.url)`: 解析转码的url内容(只是解析一下，还是/xx/xx?xx=xx 的形式);
* `ctx.request.accepts('mp5')`: 判断 req 是否支持 'mp5';
    * 支持, 返回'mp5';
    * 不支持, 返回 false ;

* `ctx.response.type`: 网页数据类型;
    * `text` => `text/plain`: 文本;
    * `html` => `text/html`: html结构;
    * `xml` => `application/xml`: xml结构;
    * `json` => `application/json`: json结构


### 路径内参数
1. 路由设置为`/read/:idn`;
2. 请求路径`http://localhost:7777/read/110103030170?name=siyeccao`;
* 读取到的结果:
```js
// ctx.params的值
{
    idn: '110103030170'
}
```

### cookie
* `ctx.cookies.get(name, [options])`: 读取上下文请求中的cookie
* `ctx.cookies.set(name, value, [options])` 在上下文中写入cookie
