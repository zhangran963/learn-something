### 后端代理
```nginx
server {
		listen 9090;
		server_name localhost 127.0.0.1;

        location / {
            root /Users/ran/www/demo;
            index index.html index.htm;
        }

        # 以 /apis 起始的路径定向到 目标路径
        location /apis {
            rewrite  ^.+apis/?(.*)$ /$1 break;
            include  uwsgi_params;
            proxy_pass   http://api.douban.com/;
       }
}
```