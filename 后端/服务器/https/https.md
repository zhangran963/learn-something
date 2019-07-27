<!-- ### 生成证书
* `openssl req -new -nodes -sha256 -newkey rsa:2048 -keyout myprivate.key -out mydomain.csr`; -->



### Let's Encrypt
`https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx`;
1. 按操作生成 .pem 文件;
### nginx
配置: `https://www.jianshu.com/p/f7f39cb24423`;


[第三方教程](https://lestatmiao.github.io/2018/01/03/certbot-letsencrypt配置ssl证书/)
* 生成证书: `sudo certbot certonly`, 后续按提示操作;
* 证书续期: `certbot renew --force-renew`;