[阮一峰 - 跨域资源共享 CORS 详解](http://www.ruanyifeng.com/blog/2016/04/cors.html)

### 网络请求

两个概念

- AJAX: 同源的 XMLHttpRequest 请求
- CROS: 跨源的 XMLHttpRequest 请求

要点:

- 浏览器自动完成
- 检测到跨源后, 自动添加一些头信息或多一次附加请求

---

### CROS 跨域资源共享

1. 简单请求

- 条件 1: 请求方法是如下内容: HEAD GET POST
- 条件 2: 头部信息是不超过如下内容
  ```md
  Accept
  Accept-Language
  Content-Language
  Last-Event-ID
  Content-Type：只限于三个值 application/x-www-form-urlencoded、multipart/form-data、text/plain
  ```
- 浏览器: 发现本次是简单请求(肯定是 CROS), 自动添加 `Origin: http://api.bob.com`
  - Origin: 浏览器发送, 发送的页面地址
  - Access-Control-Allow-Origin: 服务器发送, 允许的页面地址
- 简单请求两种结果
  1. 正常: 返回值中带有如下值, 主要是`Access-Control-Allow-Origin`, 说明正常
     ```md
     Access-Control-Allow-Origin: http://api.bob.com
     Access-Control-Allow-Credentials: true
     Access-Control-Expose-Headers: FooBar
     Content-Type: text/html; charset=utf-8
     ```
     - Access-Control-Allow-Credentials: 是否允许(后续请求)带有 cookie, CROS 默认不允许;
       - 若运行发送 cookie, Access-Control-Allow-Origin 不能是星号;
       - 还需要浏览器开启 withCredentials 属性;
         ```js
         var xhr = new XMLHttpRequest();
         xhr.withCredentials = true;
         ```
     - Access-Control-Expose-Headers: 指定(除了 Cache-Control、Content-Language、Content-Type、Expires、Last-Modified、Pragma 以外, 这六个值直接可读取, 是基本字段)可以读取到的字段
  2. 异常:
     - 无`Access-Control-Allow-Origin`字段
     - 此字段值不是 \* 或 Origin 执行的域名(网页所在域名);

2. 非简单请求

- 约等于: **预检请求 + 简单请求**
- 有特殊的方法, 自定义的头部等情况时, 浏览器先发送一条预检请求, 通过后, 才会有正式请求
- eg: 要发送一个非简单请求:
  ```js
  var url = 'http://api.alice.com/cors';
  var xhr = new XMLHttpRequest();
  xhr.open('PUT', url, true);
  xhr.setRequestHeader('X-Custom-Header', 'value');
  xhr.send();
  ```
- 预检请求示例

  ```md
  OPTIONS /cors HTTP/1.1
  Origin: http://api.bob.com
  Access-Control-Request-Method: PUT
  Access-Control-Request-Headers: X-Custom-Header
  Host: api.alice.com
  Accept-Language: en-US
  Connection: keep-alive
  User-Agent: Mozilla/5.0...
  ```

  - Origin: 来源
  - Access-Control-Request-Method: PUT, 是否允许这个方法
  - Access-Control-Request-Headers: X-Custom-Header, 是否允许这个头部,逗号分隔的字符串

- 正常返回示例

  ```md
  HTTP/1.1 200 OK
  Date: Mon, 01 Dec 2008 01:15:39 GMT
  Server: Apache/2.0.61 (Unix)
  Access-Control-Allow-Origin: http://api.bob.com
  Access-Control-Allow-Methods: GET, POST, PUT
  Access-Control-Allow-Headers: X-Custom-Header
  Content-Type: text/html; charset=utf-8
  Content-Encoding: gzip
  Content-Length: 0
  Keep-Alive: timeout=2, max=100
  Connection: Keep-Alive
  Content-Type: text/plain
  ```

  - Access-Control-Allow-Origin: 允许的域名
  - Access-Control-Allow-Methods: 所有允许的方法(避免多次请求)
  - Access-Control-Allow-Headers: 允许的字段
  - Access-Control-Allow-Credentials: 是否允许发送 cookie
  - Access-Control-Max-Age: 本次预计有效期(秒)

- 后续请求
  ```md
  PUT /cors HTTP/1.1
  Origin: http://api.bob.com
  Host: api.alice.com
  X-Custom-Header: value
  Accept-Language: en-US
  Connection: keep-alive
  User-Agent: Mozilla/5.0...
  ```
  - Origin: 浏览器自动带上
- 后续响应
  ```md
  Access-Control-Allow-Origin: http://api.bob.com
  Content-Type: text/html; charset=utf-8
  ```
  - Access-Control-Allow-Origin: 每次都包含这个字段
