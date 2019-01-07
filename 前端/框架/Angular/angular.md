* `bind-xxx` `[hero]="selectedHero"` 单向,←←←
* `on-xxx` `(tap)="doSomething($event)"` 单向,→→→
* `bindon-xxx` `[(ngModel)]="hero.name"` 双向

* `*ngFor="let item of items; let index=index"` 写在item元素上, 会重复item元素(声明index后,可以使用index,从0开始);
* `*ngFor`指令加上`trackBy`提升性能,如下:
```
<li *ngFor="let item of collection;trackBy: trackByFn">{{item.id}}</li>

trackByFn(index, item) {
    return index; // or item.id
}
```
* `*ngIf="arr.length>3"` 是否显示;
* `#phone` 声明phone为变量,可在其他地方引用,如phone.value;

* `[class]="classData"` 整体更改CSS类(会替换已经存在的class);
* `[class.red]="isRed"` 是否显示`red`类,(适用更改单个class);
* `[ngClass]="currentClass"`
```
currentClass: {};
setCurrentClass(){
    this.currentClass = {
        "saveable": this.canSave,
        "modifyed": this.isUnchanged,
        "special": this.isSpecial
    }
};
```

* `[style.color]="isSpecial?'red':'green'"` `[style.font-size]="xxx"` `[style.font-size.em]="isSpecial ? 3 : 1"`更改样式;
* `[ngStyle]="currentStyle"`
```
currentStyles: {};
setCurrentStyles() {
  this.currentStyles = {
    'font-style':  this.canSave      ? 'italic' : 'normal',
    'font-weight': !this.isUnchanged ? 'bold'   : 'normal',
    'font-size':   this.isSpecial    ? '24px'   : '12px'
  };
}
```

管道操作符 (|)
`<div>this is 管道操作符{{title|uppercase}}</div>`
`<p>{{ birthday|date:"yyyy年MM月dd日 HH:mm:ss" }}</p>`输出`2017年10月20日 12:14:31`

安全导航操作符(aaa?.b)
`obj?.name` 读取obj的name值(保证即使obj=null时,应用不会崩溃);

***

### 组件间传值
* 父组件
组件名称写在子组件的`@Component>selector`中, 传值语句:`[子组件变量]="父组件变量"`
```
template: `
<app-hero-child *ngFor="let item of items" [heroo]="item" [master]="xxx">  </app-hero-child>`

export class pagepage {
    items = [{},{}];
    master = "嘿嘿嘿"
}
```
* 子组件
1.定义组件信息; 2.初始化数据;
```
template: `
    <h6>{{heroo.name1}} says:</h6>
    <p>I, {{heroo.name}}, am at your service, {{masterName}}.</p>
`

export class pagepage{
    @Input() heroo;
    @Input() master: string;
}
```


## viewchild  

* viewchild执行完后的钩子函数 `ngAfterViewInit`
* 先引入ViewChild `import {ViewChild} from "@angular/core";`

读取元素的值(不用函数传值)  
1. 在export中添加 `@ViewChild("greet") greetDiv: ElementRef;`
2. 可以用变量`greetDiv`了 `console.log(this.greetDiv.nativeElement.innerHTML)`;
```
以上的代码直接通过 querySelector() 获取页面中的元素，通常不推荐使用这种方式。更好的方案是使用 @ViewChild 和模板变量，具体示例如下：

@Component({
  selector: 'my-comp',
  template: `
    <input #myInput type="text" />
    <div> Some other content </div>
  `
})
export class MyComp implements AfterViewInit {
  @ViewChild('myInput') input: ElementRef;

  constructor(private renderer: Renderer) {}

  ngAfterViewInit() {
    this.renderer.invokeElementMethod(
        this.input.nativeElement, 'focus');
    }
}

```

使用子组件的方法
1. html子组件元素定义变量 `#child1`;
2. ts 引入子组件 `import {KidcomComponent} from "../../xxx"`;
3. ts 应用 `@ViewChild("child1") kidcom:KidcomComponent`;
4. ts 使用子元素的方法 `this.kidcom.fangfa()`;


获取DOM元素
```
import { ElementRef } from '@angular/core';  //引入ElementRef
private el: ElementRef,  //实例化
this.el.nativeElement.querySelectorAll(".conText");  //获取到DOM元素;
```

