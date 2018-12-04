### 安装1
1. `wget https://nginx.org/download/nginx-1.14.0.tar.gz`: 下载安装包
2. `tar -zxvf nginx-1.14.0.tar.gz`: 解压下载的安装包
3. (非必须, 为了方便)重命名等操作
4. `./nginx文件夹/.configure`开始运行 nginx;
5. 这是会提示` error: the HTTP rewrite module requires the PCRE library.`;
6. `sudo apt install libpcre3 libpcre3-dev`: 安装依赖项;
7. `apt-get install openssl libssl-dev`如开启 https, 还需安装的依赖项;
8. `make` 运行;
9. `make install` 运行;
10. 此时 /usr/local/ 文件夹下有 nginx 文件夹;
    * 配置文件为conf目录下的nginx.conf;
    * 启动文件在sbin目录下的nginx文件;
11. 此时本机访问 162.219.125.154:80 应该会有 nginx 的内容;

### 安装2
* `apt install nginx`;
    * `ps -ef|grep nginx`: 查看 nginx 的运行路径;
    * `nginx -t`: 查看 nginx 的配置文件路径;



### 403 Forbiden
* 以下情况都有可能:
    * 配置文件顶部`#user  nobody;`改为`user root`或`user ran`;
    * 文件夹处改权限`chmod -R 777 /root/web-static`;
    * 保证文件夹下有对应的`index.html`;