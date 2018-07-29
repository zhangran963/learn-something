### 配置 ss
1. `wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh`: 下载安装包;
2. `chmod +x shadowsocks.sh`;
3. `sudo ./shadowsocks.sh 2>&1 | tee shadowsocks.log`: 启动, 加上`sudo`是要有 root 权限;
4. 其他就是设置密码 / 端口 之类的;