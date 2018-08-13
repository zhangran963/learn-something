### 启动/关闭 服务
* `pm2 start 服务文件`: 开启服务 app.js
* `pm2 start 服务文件 --name "server"`: 开启服务(叫 server)
* `pm2 stop 服务名`: 关闭 某个服务;
* `pm2 restart 服务名`: 重启某个服务;
* `pm2 delete 服务名`: 删除服务;


### 常用
* `pm2 start xxx --watch`: 启动并监控更改;



### 进程
* `pm2 ls`: 查看全部进程;
* `pm2 show 号码`: 某进程详情;
* `pm2 logs 名称`: 查看某一个进程的 log记录;


### 日志
* `pm2 logs 名称`: 查看某服务的console.log;
* `pm2 logs all`: 查看全部的 console.log;
* `pm2 flush`: 清除 console.log;