### Promise 和 subscribe 的区别
> Promise
* pending>resolved / pending>rejected; 一旦数据确定不再改变;
* 许诺未来某个时间执行,在then调用后, 会在未来某个时间把 result/error 发送给 then;
* 不需要 then 就可执行;
* then执行后返回新的 promise 可以继续执行 then;


> subscribe(更像同步)
* 不订阅不执行;
* 执行后返回subscriber,用于取消订阅`.unsubscribe()`;


### 原生 http 请求
```
let request: XMLHttpRequest;

if(window.XMLHttpRequest){
    request = new XMLHttpRequest();
}else{
    request = new ActiveXObject("Microsoft.XMLHTTP");
}

request.open("get", "http://localhost:8080")
request.setRequestHeader("Content-Type", "application/x-www-form-urlendcoded");
request.send("name=siyecao");
request.onreadystatechange = function () {
    if(request.readyState === 4){
        if(request.status === 200){

        }
    }
}
```

### 获取页面元素
1. 
```
** html **
<input type="text" #MyInput />

** js **
import { ViewChild } from "@angular/core";

@ViewChild("MyInput") myInput: Element;

let target = this.myInput.nativeElement;
target.value;  // input的值;
```
2. 
```
** html **
import { ElementRef } from "@angular/core";

@Component({
    selector: "my-app",
    templateUrl: "xxx",
})

export class AppComponent {
    constructor(
        private elementRef: ElementRef,
    ){
        let divEle = this.elementRef.nativeElement.querySelector("div")
    }
}

** js **



```


### 获取子组件内容
```
** parent **
import { 组件 } from "../xxx";

@ViewChild(PhotosComponent) private photosComponent: PhotosComponent;

this.photosComponent.方法/属性;
```

### 数据: 父>子
```
** parent **
<photos [maxPhotoNumber]="4"></photos>

** child **
@Component({
    ...
    inputs: ["maxPhotoNumber"],
})
export class PhotosComponent {
    maxPhotoNumber: number;

    ...
    this.maxPhotoNumber;
}
```


### 指令
```
** html **
<p class="first" SearchBackgroundColor [heighlightText]="searchText"> 内容 </p>

** Directive **
@Directive({
    selector: '[SearchBackgroundColor]',
})
export class BackgroundcolorDirective {
    @Input(): heighlightText: string;

}



```