**Ruby相关**  
先ruby软件文件夹下打开"Start Command Prompt with Ruby"
1. gem install sass 安装sass
2. gem update sass 升级sass
3. sass -v 查看版本
4. sass -h 帮助命令

1. sass test.scss \\显示代码内容;
2. sass test.scss test.css \\把test.scss的文件生成test.css

**编译**  

单文件转换
> `sass test1.scss test2.css`

单文件监听
> `sass --watch test1.scss:test2.css`

文件夹监听
> `sass --watch sassFileDirectory:cssFileDirectory`

css文件转成sass/scss文件
> `sass-convert style.css style.sass`  
`sass-convert style.css style.scss`
