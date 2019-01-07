#### 初始化
> `ionic start xxx [类型]`
类型有:
1. tabs: 下面有三栏的布局;
2. sidemenu:左侧滑动展开布局;
3. blank: 一个空页;
4. super: starter project with over 14 ready to use page designs;
5. tutorial: a guided starter project;

#### 启动
> `cd xxx` and `ionic serve`

### 打开Android/iOS/wphone形式
> `http://localhost:8100/ionic-lab`

### 新建页面
* `ionic g page login`新建登录页

### 生成apk文件
* `ionic cordova build android`

### 真机调试
* `ionic cordova run android`自动传输到真机并重启;



### 具体语法
* 输入内容```
<ion-item>
    <ion-label fixed>账号</ion-label>
    <ion-input type="text" placeholder="请输出账号" #username></ion-input>
</ion-item>
```
* 加入`no-lines`属性可以去掉底部线条;
* `this.navCtrl.push(TabsPage);`配合`import { TabsPage } from "../tabs/tabs";`实现页面跳转;
* 插入图标(存放在`http://ionicons.com/`),选中`ion-`后的名字,填入`{root: SettingPage,tabTitle: '设置',tabIcon: 'help-buoy'}`的图标处;
* `*ngFor="let item in items"` 设置html中的属性;循环从数组中取出元素;
* `*ngIf="false"` `*ngIf="a>b"` 根据条件决定是否显示或隐藏这个元素;
* `[style.color]="变量"` 在HTML中设置样式;(`[style.background-color]="'yellow'"`未生效)
* `[style.font-size.px]="20"` 设置字体大小;
* `[ngStyle]="{color:'green','background-color':'lightgray','font-size.px':20}"` 统一设置样式;
* 字体样式`font-size.px` `font-size.em` `font-size.%` 都能生效;
* `[ngClass]="{bordered: isBordered}"` 通过ts文件动态设置class;
* `ngNonBindable` 不绑定属性,设置后,双花括号中的字符串会显示出来;
```
<div ngNonBindable>
    {{我不会被绑定}}
</div>
```
* `background-image: url(../assets/imgs/头像.png);` 可以在web和app中同时看到图片

* 开启网络请求: 在app.module.ts中加入`import { HttpModule } from '@angular/http';` 并且在imports中插入`HttpModule`

* 二级页面隐藏tabs
```
imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp,{
        tabsHideOnSubPages: 'true'
    })
  ],
```

### platform
* `this.platform.exitApp()`退出APP;
* `this.platform.height()`获取高度;

### 跨域
```
,
  "proxies": [
    {
      "path": "/api",
      "proxyUrl": "http://192.168.1.249:8081/api"
    }
  ]


,
  "proxies": [
    {
      "path": "/api/",
      "proxyUrl": "http://192.168.1.249:8081/api/"
    }
  ]
```

### 全局变量
这样的方法和变量,被其他页面引用后可以直接更改;如果引入页面html中, 必须转成本页面变量`this.global = XXX.yyyyyy`;
```
export class XXX {
    public static xxxxxx;
    public static yyyyyy;
}
```

### 生成图标和启动图
1. 图标和启动图移到`resources`文件夹下;
2. 重命名 图标>`icon.png`, 启动图>`splash.png`;
3. `ionic cordova resources` 自动生成;


### 版本&名称
* 版本`~/config.xml`里的`<widget id="io.ionic.starter" android-versionCode="2" version="1.0.99" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">`, 
    * `version`: 版本号(手机上显示的版本号);
    * `android-versionCode`: (用于升级的号码);
    * `id`: packageName(没用到)
* 名称`~/config.xml`里的`<name>运维系统搜索</name>`: 应用名称;
```
1. import { AppVersion } from '@ionic-native/app-version';
2. private appVersion: AppVersion,
3. // 获取版本
    this.appVersion.getVersionNumber().then((result)=>{
        this.thisAppVersion = result;
    });
   // 类似有
   this.appVersion.getAppName();
   this.appVersion.getVersionCode();
   this.appVersion.getPackageName();
```


### 升级 cordova-android
* `ionic cordova platform update android@6.3.0 --save`; 仅升级本地的包



心得:
1. 在xxx.ts的constructor中, model.ts中的数据赋值后, 再次改变model中的数据, 页面相应改变;
2. 预计: component.ts中, 引入model数据, 若有交互数据, 直接修改model即可;
