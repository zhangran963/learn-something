* `http://www.iterm2.com/`官网下载安装文件;
* `菜单>iTerm2>make iTerm2 default term`设置终端;
* `菜单>iTerm2>preferences / keys>Hotkey>(设置全局快捷键)`


### 快捷键
* `Command + ;`根据历史记录补全;
* `Command + enter`进入全屏模式;
* `Command + n` 创建新窗口;
* `Command + d` 纵向分屏;
* `Command + shift + d` 横向分屏;

 



### 特色
* `双击`选中词(并复制);
* `三击`选中行(并复制);
* `四击`智能选中(按配置, 网址/邮箱/"字符串"等)(并复制);




***

## oh-my-Zsh

***

* 打开终端，先安装 git（已经安装的跳过该步骤），输入命令：`brew install git`;
* 打开终端，安装 wget 工具，输入命令：`brew install wget`;
* 打开终端，安装 Zsh：`brew install Zsh`;
* 打开终端，安装 oh-my-Zsh：`sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-Zsh/master/tools/install.sh -O -)"`;
    * 下载完后,提示输入用户密码, 后转换成 Zsh 形式;
    * 关掉窗口, 再次打开终端;


### Zsh特色
* 不区分大小写;
* 按`tab`键, 自动提示;
    * 再次按`tab`键, 进入选择模式;
    * `tab`: 下一项;
    * `shift + tab`: 上一项;
* `kill + 空格键 + tab键`: 列出运行的进程;
* `ls *.png`: 查找 .png 文件;
* `ls **/*.png`: 递归查找 .png 文件;
* `ls **/*`: 递归显示文件夹和文件;
* `..`或`../../`返回上一页等,不用输入 cd;
