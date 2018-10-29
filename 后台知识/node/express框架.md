

**解析post**
```js
var bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
```



**GET/POST请求**
* `var url = require("url");`: url中包含有`"/first/:name"`此种样式，可以用`req.params.name`代表`:name`
