### history模式
* 采用 history 模式的路由, vue-router 需配置成如下: 
```sh
# vue-router 采用 history 模式, nginx 做配置
location / {
  root /root/pwa-vue1/dist/;
  try_files $uri /index.html;
}


# 转发node接口服务
location /api/ {
  proxy_pass http://localhost:9091/api/;
}
```