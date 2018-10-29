### 安装
* `npm install --save koa-route`

### 简单示例
```js
const Koa = require("koa");
const route = require("koa-route");

const app = new Koa();

let main = (ctx) => {
    ctx.response.body = "主页面";
};
let first = (ctx) => {
    ctx.response.body = "first page";
};

app.use( route("/", main) );
app.use( route("/first", first) )
```



### 子路由
* 有总路由 router , 对应 `/ => mainRouter; /page => pageRouter`;
```js
let router = new Router(), main = new Router(), page = new Router();

/* 定义子路由 */
main.get("/index", (ctx, next) => {
    ctx.body = `<p>main.html</p>`
});
page.get("/index", (ctx, next) => {
    ctx.body = `<p>page.html</p>`
});

/* 装载所有路由 */
router.use('/', main.routes(), main.allowedMethods())
router.use('/page', page.routes(), page.allowedMethods())

// 加载路由中间件
app.use(router.routes()).use(router.allowedMethods())
```
* 此时, 访问`/index`到 main.html; 访问`/page/index`到 page.html;



### 获取数据 get
1. 上下文直接获取
    * `ctx.query`: 数据组成的对象;
    * `ctx.querystring`: 数据字符串;
2. request 对象中获取
    * `ctx.request.query`: 数据组成的对象;
    * `ctx.request.querystring`: 数据字符串;


### 获取数据 post
* koa并没有提供直接解析 post数据的方法; 可用`npm install --save koa-bodyparser`处理;
* 解析出来的数据对象在 `ctx.request.body` 中;
> 注意：ctx.request是context经过封装的请求对象，ctx.req是context提供的node.js原生HTTP请求对象，同理ctx.response是context经过封装的响应对象，ctx.res是context提供的node.js原生HTTP请求对象
```js
router.post("/data", (ctx, next) => {
    let data = ctx.request.body;  /* 数据 */
    /* 数据处理中... */
    ctx.body = "收到了"  /* 页面响应 */
});
```
