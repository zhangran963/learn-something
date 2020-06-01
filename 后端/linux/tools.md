### 查找 文件&文件夹
* `find / -name "nginx.conf"`: 搜索nginx.conf
* `find / -name "tomcat7" -type d`: 查找 tomcat7 文件夹;
* `find / -name 'gulpfile.js' | sort`: 查找文件并排序;
* `find ./src -type f -name "*.js" | xargs grep "abc.png"`: 查找文件(-type f), 名称(-name '*.js'), 包含文本'abc.png'的行内容;
  ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200601110124.png)


### 新建删除等
* `rm xxx`删除文件
* `rmdir xxx`删除空文件夹
* `mkdir xxx`新建文件夹
* `rm xxx` 删除文件/文件夹
* `rm -rf xxx`强制删除文件/文件夹(无提示)
* `touch xxx`新建xxx文件 或 更新文件创建时间(默认);

### 移动/复制等
* `mv 文件或文件夹 目标文件夹`: 移动文件或文件夹到其他文件夹;
* `cp -r 文件夹 目标文件夹`: 复制文件夹到目标文件夹;
* `cp 文件名 目标文件夹`: 复制文件到目标文件夹;

### 重命名文件或文件夹
* `mv 文件(夹)名 新文件(夹)名`: 重命名和移动是同一个命令;

### 压缩
`tar -zxvf 文件名`: 解压缩 文件名(tar格式)为文件夹
`zip 压缩后文件名.zip *.jpg`: 压缩 文件名(zip格式)

### 解压缩
`upzip xxx.zip`: 解压缩zip文件;

***
文件传输
***
### 下载远程文件
* `scp -P 29707 root@162.219.125.154:/root/www/hello/index.css /Users/ran/Desktop`
* `scp -P 端口号 登录名@域名或IP:远程文件地址 本地地址`

### 下载远程文件夹
* `scp -P 29707 -r root@162.219.125.154:/root/www/ /Users/ran/Desktop`
* `scp -P 端口号 -r 登录名@域名或IP:远程文件夹地址 本地地址`

### 远程上传文件
* `scp -P 29707 /Users/ran/Desktop/pic.png root@162.219.125.154:/root/`
* `scp -P 端口号 本地文件地址 登录名@域名或IP:远程地址`

### 远程上传文件夹
* `scp -P 29707 -r /Users/ran/Desktop/find root@162.219.125.154:/root/`
* `scp -P 端口号 -r 本地文件夹地址 登录名@域名或IP:远程地址`



### 搜索
grep [搜索内容] [在某某文件中]
![grep示例](https://tva1.sinaimg.cn/large/006y8mN6ly1g97qr6wc4ij30sg07ojsw.jpg)



```sh
#!/bin/bash
rootPath=$PWD

# 上传文件并排除某些内容
rsync -av -e ssh --exclude='node_modules' --exclude='.git' ${rootPath}/../mine-server root@39.106.53.163:/home/ran/www/
# rsync -av -e ssh --exclude-from='/Users/ran/www/mine-server/exclude-from.txt' ${rootPath}/../mine-server root@39.106.53.163:/home/ran/www/

echo "更新完成"


# /* exclude-from.txt 的内容是:start */
# .git/* 
# node_modules/*
# /* exclude-from.txt 的内容是:end */
```