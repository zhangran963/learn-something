* `npm install --save koa-static`;
```js
/**静态文件 */
const path = require("path");
const Static = require("koa-static");
app.use(Static(path.join(__dirname, "./public")));

```