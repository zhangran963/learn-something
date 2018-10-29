[文章链接](https://blog.csdn.net/u012758088/article/details/78598894)


# linux 安装 mongodb
1. `wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.0.0.tgz`: 下载 mongodb 安装包;
2. `tar -zxvf mongodb-linux-x86_64-3.4.10.tgz`解压此安装包;
3. `mkdir db`: 创建个文件夹用于存数据;
4. `mkdir logs`: 创建个文件夹用于存日志;
5. `cd logs && touch mongodb.log`: 创建 log文件 用于存日志;
6. `./bin/mongod --dbpath /root/my/mongodb/db`: 通过这种方式启动一下, 测试是否能启动;
7. 创建配置文件`mongodb.conf`:
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
8. `./mongodb-server/bin/mongod --config /root/my/mongodb-server/mongodb.conf`: 通过配置文件启动 mongodb;
9. `lsof -i :27017`: 查看27017端口的是不是 mongodb;

10. (做成系统服务, 开机自动启动)...







### shell 下进入 mongodb
* 启动 mongodb;
* `./bin/mongo`: 进入 shell(此时不带 auth 认证), 很多操作不能做;
* `use admin`: 切换库, 不同库有不同的用户;
* `db.auth(用户名, 密码)`: 用某个用户登录;




### 关闭 mongodb
* `ps -axu|grep mongo`: 查询 mongodb 的进程数;
* `kill -2 pid数`: 关闭;


### 设置用户
* `use admin`: 切换库;
* `db.createUser({user: 'root', pwd: '7', roles: ['root']})`: 创建用户密码权限等;
* `db.auth('root', '7')`: 验证刚才创建的用户;
* `db.createUser({user:'ran', pwd:'7', roles: [{role: 'readWrite', db: 'config'}]})`: 为某一个库添加用户并分配权限;

* `db.addUser("java","java")`: 修改用户密码;
* `db.system.users.find()`: 查看所有用户;


### 常用命令
1. 用户
* `show users`: 显示用户;

2. 数据库
* `use xxx`: 切换/创建 xxx 数据库;
* `show dbs`: 显示数据库列表;
* `db`: 当前数据库;
* `db.dropDatabase()` 删除数据库;
* `db.help()`: 显示更多命令;

3. 集合
* `db.books.insert({"name": "siyecao"})`: 在当前数据库的 books集合(没有就创建) 中插入数据;
* `show collections`: 显示集合列表;
* `db.createCollections(名称)`: 创建集合;
* `db.books.remove({})`: 清空 books 集合;
* `db.books.drop`: 删除 books 这个集合;


