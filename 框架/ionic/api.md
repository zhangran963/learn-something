删除元素
1. 标注`#chip1` `(click)="delete(chip3)"`;
2. ```
delete(chip: Element) {
    chip.remove();
}
```

更改值
1. 标注`<ion-checkbox [(ngModel)]="cucumber" (ionChange)="updateCucumber()"></ion-checkbox>`;
2. ```
updateCucumber() {
    console.log('Cucumbers new state:' + this.cucumber);
}
```

Spinner(微调)(小动画)
1. 类型:`ios ios-small bubbles circles crescent dots`;


路径
* background-image: 的路径设置为 `../assets/imgs/xxxx.png`;
* img src="": 的路径设置为 `assets/imgs/xxx.png`;
