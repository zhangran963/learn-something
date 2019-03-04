# 安装 mongodb
1. 下载 mongodb 文件;
2. 解压缩文件;
3. 重命名并放到`/usr/local`文件夹下(一般会放到这个地方);
4. 设置.zshrc 文件`export PATH=/usr/local/mongodb-server/bin:$PATH`;
5. 在某地址建立`data`, `logs`,等文件夹,在 logs 文件夹下建立`mongo.log`文件 , 建立`mongo.conf`配置文件;
6. 设置配置文件内容
```py
#数据库路径
dbpath=/Users/ran/Public/mongoFile/data/

#日志输出文件路径
logpath=/Users/ran/Public/mongoFile/logs/mongo.log

#错误日志采用追加模式，配置这个选项后mongodb的日志会追加到现有的日志文件，而不是从新创建一个新文件
logappend=true

#启用日志文件，默认启用
journal=true

#这个选项可以过滤掉一些无用的日志信息，若需要调试使用请设置为false
quiet=false

#是否后台启动，有这个参数，就可以实现后台运行
fork=true

#端口号 默认为27017
port=27017

#指定存储引擎（默认不需要指定）
#storageEngine=mmapv1

#开启网页日志监控，有这个参数就可以在浏览器上用28017查看监控界面
# httpinterface=true
```
7. `mongod --config /Users/ran/Public/mongoFile/mongo.conf`: 通过配置文件启动;
8. `lsof -i:27017`: 查看27017端口是否有 mongodb 服务;