### 登录
1. 用户A 获取 自己的code;
```
wx.login({
    success(res){
        res.code;  // code 值, 只能使用一次, 每次获取都会变;
    }
})
```
2. 传 code 到 后台;
```
wx.request({
    url: "getuserinfo地址",
    data: {
        code: code值
    },
    success(res){
        // 后台返回 openid;(实际还获取了 session_key, 可能有unionid)
    }
})
```
3. 后台 请求 微信服务器;
* 请求`url: https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code`;
    * `appid`: 小程序 id;
    * `secret`: 小程序密码;
    * `js_code`: 用户A 提供的 code;
    * `grant_type`: (固定字符串,authorization_code);
* 返回:
    * `openid`: 用户唯一标识(不变);
    * `session_key`: 会话密钥(不变);
    * (可能有)`unionid`: 用户在开放平台的唯一标识符;










### 查看已获取的权限
```
wx.getSetting({
    success(res){
        res.authSetting 对应的键值:
            => scope.userInfo: 用户信息
            => scope.userLocation: 地理位置信息
            => scope.writePhotosAlbum: 保存到相册
            等
    }
})

```