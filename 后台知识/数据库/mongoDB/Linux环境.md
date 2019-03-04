[文章链接](https://blog.csdn.net/u012758088/article/details/78598894)

# linux 安装 mongodb

1. `https://www.mongodb.com/download-center/community`: 下载页面地址;
1. `wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.0.0.tgz`: 找 .tgz 格式的文件, 下载 mongodb 安装包;
1. `tar -zxvf mongodb-linux-x86_64-3.4.10.tgz`解压此安装包;
1. `mkdir db`: 创建个文件夹用于存数据;
1. `mkdir logs`: 创建个文件夹用于存日志;
1. `cd logs && touch mongodb.log`: 创建 log 文件 用于存日志;
1. `./bin/mongod --dbpath /root/my/mongodb/db`: 通过这种方式启动一下, 测试是否能启动;
1. 创建配置文件`mongodb.conf`:

```py
dbpath=/root/my/db
logpath=/root/my/logs/mongodb.log
port=27017
fork=true
logappend=true
# PID File 的完整路径，如果没有设置，则没有PID文件
# pidfilepath=/usr/local/mongodb/mongo.pid
# 关闭http接口，默认关闭27018端口访问
#nohttpinterface=true
# 声明这是一个集群的分片，默认端口27018
shardsvr=true
# 设置每个数据库将被保存在一个单独的目录
#directorydb=true
# 开启认证
auth=true
# 设置开启简单的rest API,置后打开27017网页端口
#rest=true
```

-   `/opt`：用户级的程序目录，可以理解为 D:/Software，opt 有可选的意思，这里可以用于放置第三方大型软件（或游戏），当你不需要时，直接 rm -rf 掉即可。在硬盘容量不够时，也可将/opt 单独挂载到其他磁盘上使用。

8. `ln -s /opt/MongoDB/mongodb-linux-x86_64-ubuntu1804-4.0.6/bin/mongod /usr/local/bin/`, `ln -s /opt/MongoDB/mongodb-linux-x86_64-ubuntu1804-4.0.6/bin/mongo /usr/local/bin/`: 创建软链接;
9. `mongod --config /opt/MongoDB/mongodb.conf`: 通过配置文件启动 mongodb;
10. `lsof -i :27017`: 查看 27017 端口的是不是 mongodb;
11. (做成系统服务, 开机自动启动)...

### shell 下进入 mongodb

-   启动 mongodb;
-   `./bin/mongo`: 进入 shell(此时不带 auth 认证), 很多操作不能做;
-   `use admin`: 切换库, 不同库有不同的用户;
-   `db.auth(用户名, 密码)`: 用某个用户登录;

### 关闭 mongodb

-   `ps -axu|grep mongo`: 查询 mongodb 的进程数;
-   `kill -2 pid数`: 关闭;
