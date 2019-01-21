### 查看命令详细信息
`man 命令名称`: 查看某条命令的详细解释, 如`man mkdir`;


### 用终端terminal的命令
* `open ~/.ssh`打开资源管理器；
* `sudo scutil --set HostName 新的主机名`修改用户名（每一个命令前的）；

### 查看隐藏的文件
* `command shift +`图形窗口中切换隐藏文件;
* `ls -a` 查看全部文件和文件夹(包含隐藏的);
* `ls -l` 查看可见的文件和文件夹的权限等信息;
* `ls -al` 查看全部文件和文件夹的权限等信息;
* `which 命令名` 查看命令名的位置, 如`tsc`;

### 查找文件
* `find 路径 -name "*.js"` 查找文件, 返回路径;
    * 搜索的条件如下:
    * `*`代表任何长度的任何字符;
    * `?`代表任何单字符;
    * `[]`代表一定范围的字符, 如`doc[1-9]`,`[Dd]oucment`;

### 环境变量
`~/.bash_profile` 保存环境变量文件;
1. `export ANDROID_HOME=~/Library/Android/sdk`设置环境变量;
2. `source ~/.bash_profile` 使环境变量生效;
3. `echo $ANDROID_HOME` 查看环境变量;

### 配置 adb 命令
1. `cd ~`打开个人目录;
2. `open -e .bash_profile`用编辑器打开 bask_profile 文件;
3. 加上如下两行文本:
```
export PATH=${PATH}:/Users/apple/Library/Android/sdk/platform-tools
export PATH=${PATH}:/Users/apple/Library/Android/sdk/tools
```
4. 保存并关闭`.bash_profile`;
5. `source .bash_profile`使配置生效;



### 修改保存截图的默认路径
* `defaults write com.apple.screencapture location 自定义路径`: 修改;
* `killall SystemUIServer`: 使生效;


### 启用 任何来源
* 新版系统默认不显示任何来源
* 命令`sudo spctl --master-disable`可以显示出**任何来源**选项;

### 核心显卡/独立显卡/自动切换显卡
* `sudo pmset -a GPUSwitch {x}`: 用命令设置用哪个显卡;设置后立即生效;
    * 0: 核心显卡;(这个模式在15-inch的 MacBookPro 中不能用拓展)
    * 1: 独立显卡;
    * 2: 自动切换;


### 进程
1. `ps a|grep [名称]` 或 `ps -a|grep [名称]`: 查询某项目的进程;
2. `kill [PID]`: 杀掉某进程的PID;



### host 文件地址
`/etc/hosts`
