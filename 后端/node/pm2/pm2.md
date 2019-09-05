### 启动/关闭 服务
* `pm2 start 服务文件`: 开启服务 app.js
* `pm2 start 服务文件 --name "自定义名称"`: 开启服务(叫 自定义名称)
* `pm2 stop 服务名`: 关闭 某个服务;
* `pm2 restart 服务名`: 重启某个服务;
* `pm2 delete [服务名|ID]`: 删除服务;


### 常用
* `pm2 start 服务名 --watch`: 启动并监控更改;


### 日志
* `pm2 logs 名称`: 查看某服务的 log 记录;
* `pm2 logs all`: 查看全部的 log;
* `pm2 flush`: 清除 log;


### 进程
* `pm2 ls`: 查看全部进程;
* `pm2 show [ID|名称]`或`pm2 describe [ID|名称]`: 某进程详情;

### Dashboard
* `pm2 monit`: 单独窗口, 查看进程的资源消耗情况;

### 随服务器启动
1. `pm2 startup`或`pm2 startup ubuntu`;
2. 按提示输入命令: 如`sudo env PATH=$PATH:/usr/local/lib/node-server/bin /usr/local/share/.config/yarn/global/node_modules/pm2/bin/pm2 startup ubuntu -u ran --hp /home/ran`;
3. `pm2 save`;
