### 安装
* `npm install --save koa-route`

### 简单示例
```
const Koa = require("koa");
const route = require("koa-route");

const app = new Koa();

let main = (ctx) => {
    ctx.response.body = "主页面";
};
let first = (ctx) => {
    ctx.response.body = "first page";
}

app.use( route("/", main) );
app.use( route("/first", first) )
```