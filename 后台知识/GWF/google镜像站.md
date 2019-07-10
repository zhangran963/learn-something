* [github教程](https://github.com/cuber/ngx_http_google_filter_module/blob/master/README.zh-CN.md)

* 亲测: 兼容性差
    * ubuntu 18不能用, 报错, 16可以;
    * nginx 1.8.1及以下版本可以;

```sh
# 安装
apt-get install build-essential git gcc g++ make
# 下载
wget "http://nginx.org/download/nginx-1.7.8.tar.gz"
wget "http://ftp.cs.stanford.edu/pub/exim/pcre/pcre-8.38.tar.gz"
wget "https://www.openssl.org/source/openssl-1.0.1j.tar.gz"
wget "http://zlib.net/fossils/zlib-1.2.8.tar.gz"

# 解压缩
tar xzvf nginx-1.7.8.tar.gz
tar xzvf pcre-8.38.tar.gz
tar xzvf openssl-1.0.1j.tar.gz
tar xzvf zlib-1.2.8.tar.gz
```

### 下载插件
```sh
git clone https://github.com/cuber/ngx_http_google_filter_module
git clone https://github.com/yaoweibin/ngx_http_substitutions_filter_module
```

### 配置编译信息
```sh
# 进入 nginx文件夹
cd nginx-1.7.8
# 配置
./configure --prefix=/opt/nginx-1.7.8 --with-pcre=../pcre-8.38 --with-openssl=../openssl-1.0.1j --with-zlib=../zlib-1.2.8 --with-http_ssl_module --add-module=../ngx_http_google_filter_module --add-module=../ngx_http_substitutions_filter_module
# 其中 --add-module 指定两个插件的路径位置
```

### 编译
```sh
# 这步时间很长
make
sudo make install
```

### nginx.conf配置
* 位置: `/opt/nginx-1.7.8/conf`
```sh
server {
  server_name <你的域名>;
  listen 80;

  resolver 8.8.8.8;
  location / {
    google on;
  }
}
```

### nginx命令
```sh
# 真实位置
/opt/nginx-1.7.8/sbin/nginx
# 软链接
ln -s /opt/nginx-1.7.8/sbin/nginx /usr/local/bin/nginx
```



