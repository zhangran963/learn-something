# npm 路径
* `/usr/local/lib/node_modules`: 全局npm包安装的位置;
* `npm uninstall 包名称 -g`: 删除全局包(清除此包的文件夹);


* `npm config get prefix` 获取路径(用cnpm时用`cnpm config get prefix`);


C:\Program Files\nodejs\node_modules


### 插件版本
* `npm list koa`: 查看插件版本;
* `npm list -g koa`: 查看本地插件版本;
* `npm view koa versions` 查看某插件的全部版本(在线);
* `npm install -g ionic@3.15.0` 安装指定版本;


### 卸载
`npm uninstall -g ionic`