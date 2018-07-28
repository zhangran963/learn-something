### 连接服务器
1. 打开终端;
2. `ssh root@xxx.xxx.xx.xx` 连接服务器(备注: `207.148.22.93`);
或 `ssh root@xxx.xxx.xx.xx -p xxxx`带有端口号;
3. `yes` 输入一次yes;
4. `(kW69gf4]]uLJcKx` 输入密码;
5. `exit` 退出;
7. `ssh-copy-id -i ~/.ssh/id_rsa.pub root@162.219.125.154 -p 29707`: 免密码登录, 把登录机的 id_rsa.pub 文件上传到 远程机;


### 查看登录用户进程
1. `ps aux |grep sshd`列出列表;
2. `kill xxx`清除进程数;

### 查看服务进程
1. `ps -ef|grep node`: 查看 node进程;
2. `kill pid号`: 停止此进程;



### 清除旧ssh信息
`ssh-keygen -R 远程服务器IP地址`,如有类似"ECDSA host key for 45.76.14.160 has changed and you have requested strict checking"的提示时, 是因为远程服务器更新过系统,需要清除本地缓存的旧的登录信息;

### 虚拟环境
`virtualenv venv` 创建虚拟环境;
`source venv/bin/activate` 激活虚拟环境(打开);
`deactivate` 退出虚拟环境;

### vim编辑器
1. `sudo vi xxx`用vi编辑器打开文件;
2. 打开后默认是命令行模式;
3. 命令行:输入`i`进入编辑模式(注: 没有回车键);
4. 命令行:输入`a`在光标后编辑(这个更常用);
5. 命令行:输入`o`插入新的一行,在行首开始输入;
6. 命令行: `dd`删除此行;
7. 底行模式: `:wq`保存并退出;
8. 底行模式: `:q!`不保存强制退出;


### 修改密码
* 在普通用户下
* `sudo passwd root`: 更改 root 密码
* 输入普通用户密码
* 输入root新密码o
* 再次输入root新密码
* `su - root`: 切换成 root 用户状态;


### 新建删除等
* `rm xxx`删除文件
* `rmdir xxx`删除空文件夹
* `mkdir xxx`新建文件夹
* `rm xxx` 删除文件/文件夹
* `rm -rf xxx`强制删除文件/文件夹(无提示)
* `touch xxx`新建xxx文件 或 更新文件创建时间(默认);
* `getconf LONG_BIT`查看系统版本数;


### 移动/复制等
* `mv 文件或文件夹 目标文件夹`: 移动文件或文件夹到其他文件夹;
* `cp -r 文件夹 目标文件夹`: 复制文件夹到目标文件夹;
* `cp 文件名 目标文件夹`: 复制文件到目标文件夹;

### 重命名文件或文件夹
* `mv 文件(夹)名 新文件(夹)名`: 重命名和移动是同一个命令;


### 解压缩
`tar -zxvf 文件名`: 解压缩文件名为文件夹




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


### 用户
* `/root`: root 用户的地址;
* `/home/ran`: 普通用户的地址;

### 授予权限
* `chmod 777 文件夹/文件路径`: 给目标授予权限

