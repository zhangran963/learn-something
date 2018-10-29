1. 安装:`pip3 install scrapy`
    * 查看此包信息: `pip3 show scrapy`
2. 不能识别`scrapy`命令时, 创建软链接: `sudo ln -s /Library/Frameworks/Python.framework/Versions/3.6/bin/scrapy /usr/local/bin/scrapy`;



### 创建项目
1. 创建项目: `scrapy startproject 名称`
2. 进入项目名称文件夹下, 如`项目根目录/项目名称/`;
3. 创建新的 spider: `scrapy genspider 爬虫名称(不能和项目重名) "爬去网站的域名"`;
4. 设置文件:
    * `ROBOTSTXT_OBEY`值改为 `False`(是否按 robots.txt 规则爬取);
    * `headers`

### 运行项目
* `scrapy crawl 名称`