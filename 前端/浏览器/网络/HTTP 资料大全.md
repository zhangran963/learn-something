[文章链接](https://segmentfault.com/a/1190000008900299)

***

### URI 统一资源标识符
* URI的最常见的形式是统一资源定位符（URL），经常指定为非正式的网址。更罕见的用法是统一资源名称（URN），其目的是通过提供一种途径。用于在特定的命名空间资源的标识，以补充网址。—— 维基百科
```md
                       权限                 路径
        ┌───────────────┴───────────────┐┌───┴────┐
  abc://username:password@example.com:123/path/data?key=value&key2=value2#fragid1
  └┬┘   └───────┬───────┘ └────┬────┘ └┬┘           └─────────┬─────────┘ └──┬──┘
  协议        用户信息         主机名    端口                  查询参数          片段
```

***

### MIME
* 设定 **某种扩展名的文件** 用一种 **(特定)应用程序** 来打开的方式类型
* 示例: `text/html`, `text/plain`, `image/png`, `application/pdf`

***

### HTTP
* 超文本传输协议（英文：**HyperText Transfer Protocol**，缩写：HTTP）
* 特点: 
  * 无连接: 无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接，采用这种方式可以节省传输时间。(当今多数服务器支持Keep-Alive功能，使用服务器支持长连接，解决无连接的问题)
  * 无状态: 无状态是指协议对于事务处理没有记忆能力，服务器不知道客户端是什么状态。即客户端发送HTTP请求后，服务器根据请求，会给我们发送数据，发送完后，不会记录信息。(使用 cookie 机制可以保持 session，解决无状态的问题)
  * 简单快速: 当客户端向服务器端发送请求时，只是简单的填写请求路径和请求方法即可，然后就可以通过浏览器或其他方式将该请求发送就行了
  * 灵活: HTTP 协议允许客户端和服务器端传输任意类型任意格式的数据对象

***

### 请求报文
1. 请求行
    * 请求方法 &nbsp;&nbsp; URL地址 &nbsp;&nbsp; HTTP/版本
2. 请求头
    * Accept: 客户端可识别得内容类型列表 - text/html,application/xhtml+xml,application/xml
    * Host: 请求的主机名，允许多个域名同处一个IP地址，即虚拟主机
      * 如, 在 `https://todolist.thesoundofsilence.top` 中
      ![](https://tva1.sinaimg.cn/large/006y8mN6ly1g7k5buk8yrj30hs040dfq.jpg)
    * connection：连接方式
      * close：告诉WEB服务器或代理服务器，在完成本次请求的响应后，断开连接
      * keep-alive：告诉WEB服务器或代理服务器。在完成本次请求的响应后，保持连接，以等待后续请求, HTTP/1.1支持
    * Cookie：存储于客户端扩展字段，向同一域名的服务端发送属于该域的cookie
3. 空行
4. 请求体
  * 只在 POST方法中使用
  * 响应中的有关参数: `Content-Length`, `Content-Length`

```md
GET / HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,id;q=0.4
Cookie: PSTM=1490844191; BIDUPSID=2145FF54639208435F60E1E165379255; BAIDUID=CFA344942EE2E0EE081D8B13B5C847F9:FG=1;
```

***

### 响应报文
```md
HTTP/1.1 200 OK
Server: bfe/1.0.8.18
Date: Thu, 30 Mar 2017 12:28:00 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Cache-Control: private
Expires: Thu, 30 Mar 2017 12:27:43 GMT
Set-Cookie: BDSVRTM=0; path=/
```
1. 状态行
    * HTTP/协议版本 状态码 状态码描述
2. 响应头
    * Date: 服务器时间
    * Content-Type: 资源类型
    * Connection:
      * close: 连接已关闭
      * keep-alive: 连接保持中, 可用用后续请求
    * Cache-Control: 缓存控制
    * Expires: 设置过期时间
    * Set-Cookie: 设置Cookie信息
3. 空行

4. 响应体
```md
<!DOCTYPE html>
<!--STATUS OK-->
<html>
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu.svg">
    <title>百度一下，你就知道</title>
</head>
<body>
  ...
</body>
</html>
```




