### 查看 Node 路径

- `npm config get prefix`
  ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200120175228.png)

### 源地址

- `npm config get registry`: 查看源
  ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200120175355.png)
- 更改源到淘宝源: `npm config set registry https://registry.npm.taobao.org`
- 恢复官方源: `npm config delete registry`

### 插件版本

- `npm list koa`: 查看插件版本;
- `npm list -g koa`: 查看本地插件版本;
- `npm view koa versions`: 查看某插件的历史版本(在线);
- `npm info koa`: 包信息;
- `npm install -g ionic@3.15.0`: 安装指定版本;

### 卸载

`npm uninstall -g ionic`
