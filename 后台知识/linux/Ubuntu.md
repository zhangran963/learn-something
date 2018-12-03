### 连接服务器
1. 打开终端;
2. `ssh root@xxx.xxx.xx.xx` 连接服务器(备注: `207.148.22.93`);
或 `ssh root@xxx.xxx.xx.xx -p xxxx`带有端口号;
3. `yes` 输入一次yes;
4. `(kW69gf4]]uLJcKx` 输入密码;
5. `exit` 退出;
7. `ssh-copy-id -i ~/.ssh/id_rsa.pub root@162.219.125.154 -p 29707`: 免密码登录, 把登录机的 id_rsa.pub 文件上传到 远程机;


### 清除服务器后, 再次连接服务器
* 用 ssh 连接过服务器, 客户端会生成一个认证, 如果直接连接 同IP的新服务器, 会报错"WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!";
* 清除旧认证`ssh-keygen -R [服务器IP]`;
* 再次连接即可;


### 查看*登录用户*进程
* 登录的用户, 某些 ssh 登录超时, 窗口不能操作了, 在这还显示登录中;
1. `ps aux|grep sshd`: 列出登录用户列表;
2. `kill xxx`清除此登录用户;

### 查看服务进程
1. `ps -ef|grep node`: 查看 node进程;
2. `kill 第一个数字(pid号)`: 停止此进程; 

### 查看端口运行的服务
* `lsof -i:27017`: 查看27017端口的是不是 mongodb;



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





### 授予权限
* `chmod 777 文件夹/文件路径`: 给目标授予权限

### sshd
* 查看sshd服务的网络连接情况：`netstat -ntlp`
* 启动服务: `systemctl start sshd.service`
* 查看服务状态: `systemctl status sshd.service`
* `netstat -antlp|grep sshd`

