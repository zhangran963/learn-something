## 压力测试
`ab -c 50 -n 1000 http://39.106.53.163:3001/ip`
* c: 并发数
* n: 请求数


### 仅需要 cookie
`ab －n 100 －C key＝value http://test.com/`


### 需要多个token，直接设Header：
`ab -n 100 -H “Cookie: Key1=Value1; Key2=Value2” http://test.com/`

![](https://tva1.sinaimg.cn/large/006tNbRwly1g9il7t6omgj30rs0ulgnr.jpg)<style>img {max-width: 400px} .w4{max-width: 400px}.w5{max-width: 500px}</style>

