1. `wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.0.0.tgz`: 下载 mongodb 安装包;
2. `tar -zxvf mongodb-linux-x86_64-3.4.10.tgz`解压此安装包;
3. `mkdir db`: 创建个文件夹用于存数据;
4. `mkdir logs`: 创建个文件夹用于存日志;
5. `cd logs && touch mongodb.log`: 创建 log文件 用于存日志;
6. `./bin/mongod --dbpath /root/my/mongodb/db`: 通过这种方式启动一下, 测试是否能启动;
7. 创建配置文件`mongodb.conf`:
```
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
# 设置开启简单的rest API,置后打开28017网页端口
#rest=true
```
8. `./mongodb-server/bin/mongod --config /root/my/mongodb-server/mongodb.conf`: 通过配置文件启动 mongodb;
9. `lsof -i :27017`: 查看27017端口的是不是 mongodb;