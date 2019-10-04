### 安装homebrew
* `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

### 常用
* `brew search <包名称>` 查询包信息;
    * 如 安装node时, 输入的版本是`node@10`, 最终安装的版本是`v10.16.0`; 
* `brew install <包名称>`安装;
    * 实例, 输入查询到的版本号`brew install node@10`;
* 有时安装完, 不能识别命令, 再次输入 `brew link node@10`
    * `brew link --overwrite --force node@10`: 覆盖旧信息并link;
* `brew uninstall <包名称>`卸载;
* `brew outdated` 查看是否有包需要更新;
* `brew upgrade <包名称>` 更新包;
* `brew list --versions` 查询已安装包(显示版本号);
* `brew -h` 查看brew的命令;
* `brew info <包名称>` 查询这个包的信息;
* `brew cleanup`: 清除缓存?;