1. `vue init webpack 项目名称`: 创建基于 webpack 的vue项目;
2. `cd 项目名称`: 打开项目;
3. `npm run dev`: 运行项目;


* 使用`Vue`需要先引入`import Vue from 'vue' `;
* 使用`Router`需要先引入`import Router from 'vue-router' `;


### 配置的路径
* 使用方式, 引入页面:`import HelloWorld from '@/components/HelloWorld'`;
* 配置方式, webpack.base.conf.js 中, `resolve>alias>'@': resolve('src')`;

### 引入文件的方式
* `import test from './router'`: 直接引入父文件夹名, 默认找文件夹中叫`index.js`的文件, 没有报错;
* `import test from './router/self'`引入文件夹名和文件名;



`router index.js`是路由;
`App.vue`是首页;
`components/xxx.vue`是组件,填充页面用的;


### Vue 项目的跨域设置
在`/config/index.js`中, 
```js
module.exports = {
    dev: {
        ...
        proxyTable: {
            // 监听带有'/kuayu'的字符串
            '/kuayu': {
                target: 'http://localhost:7001', // 设置你调用的接口域名和端口号
                changeOrigin: true, // 跨域
                pathRewrite: {
                    '^/kuayu': '/'    // 把'/kuayu'替换成'/'
                }
            }
        }
        ...
    }
}
```