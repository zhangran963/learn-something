### 创建 shadowsocks 服务端

1. 购买服务器, 设置登录账号等需要提前完成;

2. 安装 shadowsocks 服务器端;

- 方法 1: 自动处理

  - 已包含 多端口/加速 等设置; 端口号 43340~43360; 具体请查看 `auto.sh`
  - 下载自动执行文件: `wget https://raw.githubusercontent.com/Clayder-ran/learn-something/master/Google%20Cloud/auto.sh`
  - 或 创建文件, 如`auto.sh`, 内容是 本文件的同级文件`./auto.sh`
  - 执行, `. auto.sh`
  - 后续输入 密码/端口号/加密方式; 等待结束即可; 配置项会打印出来;

- 方法 2: 手动处理

  - 下载 shadowsocks 软件: `wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh`;
  - 权限: `chmod +x shadowsocks.sh`;
  - 设置: `sudo ./shadowsocks.sh 2>&1 | tee shadowsocks.log`
  - 按提示输入 密码/端口号/加密方式; 按"任意按键"开始安装;

---

### 开启 TCP BBR 拥塞控制算法 (加速)

(加速不是必须)
[参考教程地址](https://github.com/iMeiji/shadowsocks_install/wiki/开启TCP-BBR拥塞控制算法)

1. 检查条件:
   - 查看内核 `uname -r`, 需要内核>=4.9, "Ubuntu 18.04 LTS"是 4.15, 满足条件;
2. 开启, 依次执行以下命令(没有权限时, 命令前添加 `sudo`);

   - `modprobe tcp_bbr`;
   - `echo "tcp_bbr" | sudo tee --append /etc/modules-load.d/modules.conf`;
   - `echo "net.core.default_qdisc=fq" | sudo tee --append /etc/sysctl.conf`
   - `echo "net.ipv4.tcp_congestion_control=bbr" | sudo tee --append /etc/sysctl.conf`
   - `sysctl -p`: 保存生效

3. 检测结果:
   - 输入`lsmod | grep bbr`, 有"tcp_bbr"模块, 就是已经开启了 BBR;

---

### 其他

- 查询占用端口: `lsof -i:43352`
- 配置文件路径: `/etc/shadowsocks.json`
- 自动执行的配置: `./auto.sh`
- 多端口的配置: `./shadowsocks.json`

- 启动服务: `ssserver -c /etc/shadowsocks.json -d start`
- 停止服务: `ssserver -d stop`
- 重启服务: `ssserver -d restart`
- 卸载服务: `./shadowsocks.sh uninstall`
