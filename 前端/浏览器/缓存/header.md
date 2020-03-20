[教程地址](https://www.cnblogs.com/shixiaomiao1122/p/7591556.html)  
[MDN Cache-Control](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Cache-Control)  

---

* 缓存文件位置: chrome 浏览器 > `chrome://chrome-urls/` > 找到 `chrome://cache` ; 
![缓存文件头部](https://tva1.sinaimg.cn/large/006y8mN6gy1g7ltv0vhb9j30qa0d8dgg.jpg)

* Date 请求此文件时的(服务器)时间;
* Expires (服务器)指明文件过期时间(http1.0 标准, 优先级低);
* Cache-Control 使用相对时间(http1.1 标准, 优先级高);

  + max-age 缓存的最大有效时间, 单位秒(s), 覆盖 expires;
  + public: 响应可以被任何对象(客户端+代理服务器等(能用于多用户共享))缓存;
  + private: 私有缓存(单个用户使用, 代理服务器不能缓存);
  + no-cache/max-age=0: 强制确认缓存; 可以缓存, 但每次都要重新验证;
  + no-store: 绝对禁止缓存;
  + s-maxage: 只用于共享缓存, 如 CDN; 
  + must-revalidate: 如果页面过期, 则去服务器获取; 

* Last-Modified(服务器返回) <=> If-Modified-Since(下次, 浏览器请求)

  1. Last-Modified: 请求文件时, 服务器标识的 `文件最后修改时间`; 
  2. If-Modified-Since: 下次浏览器再次请求时, 若`资源过期: Date+max-age(Cache-Control中) < 当前时间` 并且 `有Last-Modified属性`, 则带上 `If-Modified-Since`, 用于服务器判断是否文件修改, 返回 HTTP200(新内容) / HTTP 304 (旧内容,无需包体，节省流量); 

* Etag(服务器返回) <=> If-None-Match(下次, 浏览器请求)

  + Etag: 按服务器规则(apache 中是索引节+大小+修改时间的 hash 值)生成的唯一标识; 
    + If-Modified-Since: 浏览器再次请求时, `资源过期: Date+max-age(Cache-Control中) < 当前时间` 并且 `有Etag属性`, 则带上 If-None-Match, 用于服务器判断是否文件修改: 返回 HTTP200(新内容) / HTTP 304 (旧内容,无需包体，节省流量); 

* Last-Modified 和 Etag 的区别
  + Last-Modified 判断的是修改时间; Etag 判断的是文件内容+修改时间; 
  + 优先级: Etag > Last-Modified; 先判断 Etag, 一致后再对比 Last-Modified; 
  + Last-Modified 的精确度只到秒级, 如果一秒内多次修改, 会有判断不准确的情况; 
  + 有的文件是定期自动生成的(实际内容不变), Last-Modified 会修改, 但 Etag 不会变; 

# 继续看

`https://www.cnblogs.com/shixiaomiao1122/p/7591556.html` 

