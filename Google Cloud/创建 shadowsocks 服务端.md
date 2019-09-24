### 谷歌云平台创建shadowsocks服务端的主要过程:
前提, 已经有 google账号, 能翻墙操作谷歌云后台;
1. 登录谷歌云`https://cloud.google.com`; 登录google账号, 获取优惠(我忘记我获取过程了, 但很简单, 或者在网上找找?);
    * $300优惠, 有效期一年;
2. 找到控制台, 创建一个项目;
3. 左侧的 Compute Engine 中, 上侧 [创建实例];
    * 名称, 随便;
    * 区域和地区, 随便;
    * 启动磁盘, 最好选"Ubuntu 18.04 LTS", 原因:
        * 方便做加速, 内核>4.9;
        * 我用的这个版本, 其他版本可能以下命令不适用;
    * 防火墙, 允许 HTTP 和 HTTPS 流量;
4. 保存后, 创建实例中, 稍等一会, 创建成功;
    * 注: 默认情况, 实例中的外部ip, 每重启一次实例, 就会改变ip, 可以设置为静态ip, 教程`http://justcode.ikeepstudying.com/2017/11/google-cloud-platformgcp-vm-固定静态外部ip设定/`;
5. 通过 [ssh] 连接;
    * 方式1, 实例右侧的[ssh], 在网页中操作;
    * 方式2, 终端中输入命令: `ssh 用户名@ip地址`(1. 这次应该不行, 不知道密码 2. 可以设置默认登录等更方便的方式, 记录在`https://github.com/Clayder-ran/learn-something/tree/master/后台知识/linux`中);
6. 等一会, 远程连接中
7. 远程登录后, 此时登录的是自己的谷歌账号;
8. 创建并切换到 root 账号(好处: 权限大);
    * `sudo passwd root`: 创建 root 用户密码
    * 输入两次相同的密码, 创建成功;
    * `su - root`: 切换当前账号 到 root账号;
9. 开始安装 shadowsocks 服务器端;
    * 下载 shadowsocks 软件: `wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh`;
    * 权限: `chmod +x shadowsocks.sh`;
    * 设置: `sudo ./shadowsocks.sh 2>&1 | tee shadowsocks.log`;
        1. 密码
        2. 端口
        3. 加密方式
        4. 按"任意按键"开始安装;
10. 一会儿(最低配机器, 用了10分钟)安装完成
11. 打印出ip/密码等结果, 服务自动启动, 可在本地电脑做链接测试;

```
IP地址: 35.220.218.17
端口: 43352
密码: 777777
加密方式: rc4-md5
```


### 开启TCP BBR拥塞控制算法 (加速)
(加速不是必须)
[参考教程地址](https://github.com/iMeiji/shadowsocks_install/wiki/开启TCP-BBR拥塞控制算法)

1. 检查条件:
    * 查看内核 `uname -r`, 需要内核>=4.9, "Ubuntu 18.04 LTS"是4.15, 满足条件;
2. 开启, 依次执行以下命令(没有权限时, 命令前添加 `sudo`);
    * `modprobe tcp_bbr`;
    * `echo "tcp_bbr" | sudo tee --append /etc/modules-load.d/modules.conf`;
    * `echo "net.core.default_qdisc=fq" | sudo tee --append /etc/sysctl.conf`
    * `echo "net.ipv4.tcp_congestion_control=bbr" | sudo tee --append /etc/sysctl.conf`  
    * `sysctl -p`: 保存生效
4. 检测结果:
    * 输入`lsmod | grep bbr`, 有"tcp_bbr"模块, 就是已经开启了 BBR;



### 退出系统
* `exit` 或 `logout`




查询占用端口: `lsof -i:43352`
配置文件路径: `/etc/shadowsocks.json`
启动服务: `ssserver -c /etc/shadowsocks.json -d start`
停止服务: `ssserver -d stop`


### 多端口
* 用配置文件替换服务器中的配置
* `scp ~/Documents/GitHub/knowledgement/Google\ Cloud/shadowsocks.json root@45.77.12.228:/etc/`
```json
{
    "server":"0.0.0.0",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "port_password":{
        "43340":"777777",
        "43341":"777777",
        "43342":"777777",
        "43343":"777777",
        "43344":"777777",
        "43345":"777777",
        "43346":"777777",
        "43347":"777777",
        "43348":"777777",
        "43349":"777777",
        "43350":"777777",
        "43351":"777777",
        "43352":"777777",
        "43353":"777777",
        "43354":"777777",
        "43355":"777777"
   },
    "timeout":300,
    "method":"aes-256-gcm",
    "fast_open":false
}
```