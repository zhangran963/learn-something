### 开启 Grid 布局

``` css
.wrapper {
    display: grid;
    /* block模式 */
    display: inline-grid;
    /* inline-block模式 */
}
```

### 正常布局

``` css
.wrapper {
    /* 三列 */
    grid-template-columns: 200px 100px 200px;
    /* 两行，行高都为 50px  */
    grid-template-rows: repeat(2, 50px);
    /* 单元格间的间距 */
    grid-gap: 5px;
}
```

### 横向自由填充

``` css
  .wrapper {
      /* 横向自动填充; 每个200px宽 */
      grid-template-columns: repeat(auto-fill, 200px);
      grid-gap: 5px;
      /* 纵向 150px 高 */
      grid-auto-rows: 150px;
  }
```
```css
.wrapper {
  /* 横向自动填充; 平均分配; 每项最小220px宽 */
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  /* 即使某项超宽, 改变网页宽度时, 也能满填充 */
  grid-auto-flow: row dense; 
}
```

### 按比例分配

``` css
.wrapper {
    /* 200px 分完后, 剩余部分, 按比例分配 */
    grid-template-columns: 200px 1fr 2fr;
}
```
