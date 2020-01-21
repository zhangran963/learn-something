[全局nvm教程](https://segmentfault.com/a/1190000019929765)

### 全局nvm
* 在nvm下安装的node, 也是全局的

### 1. 创建目录
* `mkdir /usr/local/nvm`: 存储nvm的环境变量
* `git clone https://github.com/nvm-sh/nvm.git /opt/nvm`: 把nvm项目存入"/opt/nvm"

### 2. 创建初始用户登录脚本
* `vim /etc/profile.d/nvm.sh`
```sh
export NVM_DIR=/usr/local/nvm # 导出NVM_DIR 环境变量，让nvm 安装node到该目录
source /opt/nvm/nvm.sh # 执行nvm 的命令, 激活nvm 到系统shell 中

# 用户进来使用的node版本, 不必须
# nvm use 10.16.0 
```

### 3. 后续就是安装node的过程
* `nvm ls-remote`: 查看远程版本
* `nvm install v13.6.0`: 安装某一个版本
* `nvm uninstall v13.6.0`: 卸载某一版本