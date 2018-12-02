### 安装
`brew install yarn`

### 卸载
`npm uninstall yarn -g`:
* 经常不能卸载成功
* 手动删除文件
    ```
        rm -rf /usr/local/lib/node_modules/yarn
        rm -rf /usr/local/bin/yarn yarnpkg
    ```


### 升级
`brew upgrade yarn`

### 查看版本

`yarn --version`

### 添加依赖包
`yarn add [包名称]`
`yarn add [包名称]@[版本]`

### 升级依赖包
`yarn upgrade [包名称]`
`yarn upgrade [包名称]@[版本]`

### 移除依赖包
`yarn remove [包名称]`

### 显示 yarn安装目录
`yarn bin`
* 结果`/Users/ran/node_modules/.bin`;
* 如有文件安装完后, 不能识别命令, 设置软链接`ln -s /Users/ran/node_modules/.bin/[命令文件] /usr/local/bin/[命令名称]`


### 缓存
`yarn cache ls`: 列出缓存包
`yarn cache dir`: 显示缓存目录
`yarn cache clean`: 清除缓存


### 安装某项目的全部依赖
`yarn` 或 `yarn install`

### 查看安装的依赖包
`yarn list`

### 查看依赖包信息
`yarn info [包名称]`

### 初始化项目
`yarn init`

### 运行命令
-   `yarn run [自定义命令名称]`

```json
{
    "name": "my-package",
    "scripts": {
        "build": "babel src -d lib",
        "test": "jest"
    }
}
```
