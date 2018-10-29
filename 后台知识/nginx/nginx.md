### 正向代理 vs 反向代理

> 正向代理，是一个位于客户端和原始服务器(origin server)之间的服务器，为了从原始服务器取得内容，客户端向代理发送一个请求并指定目标(原始服务器)，然后代理向原始服务器转交请求并将获得的内容返回给客户端  
**就像 shadowsock 翻墙;**  
对于服务器而言, 代理方就像原始客户端;

> 例用户访问 http://abcd/readme 但abcd上并不存在readme页面他是偷偷从另外一台服务器上取回来，然后作为自己的内容吐给用户，但用户并不知情这很正常，用户一般都很笨这里所提到的 abcd这个域名对应的服务器就设置了反向代理功能;  
**就像前端开发中,静态文件取本地,接口取网络(接口数据用到的是反向代理)**  
对客户端而言,代理方就像原始服务器;

### 安装 nginx
* `brew info nginx`查看 nginx信息, 如有`Not installed`字样, 说明本地还未安装;
* `brew install nginx` 安装;
可能会有 Error;
```
Error: 
Could not symlink share/man/man8/nginx.8
/usr/local/share/man/man8 is not writable.
```
* 这是权限问题, 命令行输入`sudo chown -R $(ran):admin /usr/local/share/man`;
* 再次连接`brew link nginx`;


### 路径等
* `/usr/local/etc/nginx/nginx.conf`配置文件路径;
* `/usr/local/var/www`服务器默认路径, 就是存网页的文件夹;
* `/usr/local/Cellar/nginx/1.12.2_1`安装路径;

### 启动
* `nginx`;

### 关闭
* `sudo nginx -s stop`关闭 nginx;

### 重启
* `sudo nginx -s reload`重启 nginx;




***
## 下面的内容旧
***
### 查看执行结果
`ps -ef|grep nginx`
* 如果有多行, 先停止再启动 , 其中`nginx: master process`这一行的前面第二个数就是进程数;
* 如果只有一行, 可以启动;

### 启动
`/usr/local/Cellar/nginx/1.12.2_1/bin/nginx -c /usr/local/etc/nginx/nginx.conf`

### 停止
`kill -QUOT 进程数`(正常停止,不会立即停止)
`kill -TERM 进程数` 立即停止;
`kill -INT 进程数` 立即停止;

### 重启
`kill -HUP 进程数` 重启
`/usr/local/Cellar/nginx/1.12.2_1/bin/nginx -s reload` 重启(命令中版本号会不同)







### window中
* `C:\server\nginx-1.0.2>nginx.exe -s stop`强制停止nginx;
* `C:\server\nginx-1.0.2>nginx.exe -s quit`停止nginx;

* `C:\server\nginx-1.0.2>start nginx`启动nginx;

* `C:\server\nginx-1.0.2>nginx.exe -s reload`重启nginx;