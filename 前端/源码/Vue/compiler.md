compiler编译: 将template编译为render函数
存放路径: `src/compiler`

### 用webpack构建的项目
1. 把`.vue`文件用`vue-loader`做处理; template => render函数
2. 但 main.js中的template没有处理, 需要用到`vue.esm.js`(包含compiler)

