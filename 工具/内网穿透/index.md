
访问一般的网站, 需要有 公网IP + 本地端口 + 域名;
若没有公网IP, 可用内网如下命令:`ssh -R 80:域名和端口 ssh.localhost.run`;
在返回的内容中有这个结果`ran-332b14ed.localhost.run`, 可在外网访问;

示例
```sh
ssh -R 80:192.168.1.123:5555 ssh.localhost.run
```