### 用到的工具
1. `keytool` 生成签名包;
路径`/Library/Java/JavaVirtualMachines/jdk1.8.0_151.jdk/Contents/Home/bin/`;
2. `jarsigner` 写入签名信息;
路径`/Library/Java/JavaVirtualMachines/jdk1.8.0_151.jdk/Contents/Home/bin/`;
3. `zipalign` 优化(非必需);
路径 ``

### 生成签名包

`keytool -genkey -v -keystore yunwei-kuter.keystore -alias kuter-01.keystore -keyalg RSA -validity 36500`

> 说明:
* -genkey意味着执行的是生成数字证书操作 
* -v表示将生成证书的详细信息打印出来，显示在dos窗口中  
* -keystore yunwei-kuter.keystore 表示生成的数字证书的文件名为“ yunwei-kuter.keystore”(spilledyear可以取自己的名字) 
* -alias kuter-01.keystore 表示证书的别名为“kuter-01.keystore”，当然可以不和上面的文件名一样 
* -keyalg RSA 表示生成密钥文件所采用的算法为RSA 
* -validity 36500 表示该数字证书的有效期为36500天，意味着36500天之后该证书将失效

### 写入签名

`jarsigner -verbose -keystore yunwei-kuter.keystore -signedjar yunwei-kuter.apk android-release-unsigned.apk kuter-01.keystore`

> 说明:
* -verbose表示将签名过程中的详细信息打印出来，显示在dos窗口中
* -keystore yunwei-kuter.keystore 表示签名所使用的数字证书所在位置，没有写路径表示在当前目录下
* -signedjar yunwei-kuter.apk android-release-unsigned.apk 表示给android-release-unsigned.apk文件签名，签名后的文件名称为yunwei-kuter.apk 
kuter-01.keystore 表示证书的别名，对应于生成数字证书时-alias参数后面的名称

### 优化

没添加到path中, 使路径打开 `/Users/ran/Library/Android/sdk/build-tools/23.0.1/zipalign`
`zipalign -v 4 [原名].apk [新压缩名].apk`
> * -v表示在DOS窗口打印出详细的优化信息 