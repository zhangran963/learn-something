http 协议
* 默认80端口

https 协议
* 默认 443 端口


url解释
* URL 统一资源定位符
* `scheme://host:port/path/?query-string=xxx#anchor`
    * scheme: 协议;
    * host: 主机名;
    * port: 端口号;
    * path: 路径;
    * query-string: 传输数据;
    * anchor: 锚点, 用于前端页面定位;
* 发送 url 前, 需要先对 url进行编码(字母/数字/部分符号不用编码), 采用 `%+16进制码`;


发送数据
* 数据在 url中(get 请求);
* 数据在 body 中(post请求);
* 数据在 head 中;


伪造身份
* 服务器通过 header 中的 user-agent 判断身份类型;
    * 爬虫程序默认的身份是 python, 需要改成浏览器;
* Referer: 此请求的上一个 url是什么(从哪里来的);
    * 爬虫程序需要改为上一个url;

状态码
* 200: 正常, 可能给爬虫返回假数据;
* 301: 永久重定向(例 www.jingdong.com => www.jd.com);
* 302: 临时重定向, (例, 未登录时重定向到登录页);
* 400: 请求的url找不到;
* 500: 服务器错误;