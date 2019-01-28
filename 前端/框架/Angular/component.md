## 体会
* 组件专注做'用户体验相关'的事情;
* 其他 网络数据/打印/数据验证 等交给服务做;
  
---

## 依赖注入
* 根实例中注入, 生成单一共享的服务实例;  
```js
@Injectable({
    providedIn: 'root',
})
```

* 在组件中提供注册提供商,
```js
@Component({
    selector:    'app-hero-list',
    templateUrl: './hero-list.component.html',
    providers:  [ HeroService ]
})
```

* `NgModule` 相当于特殊的 注入;
```js
@NgModule({
    providers: [
        BackendService,
        Logger
    ],
    ...
})
```

---

## 过程
1. 获取全部依赖(1,2,3)
2. 组件实例化(依赖1, 依赖2, ...)

---







![图片](./0.jpg)




