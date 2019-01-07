### 在 css 上的拓展
* 尺寸单位: `rpx`屏幕宽度750rpx;
* 导入外联样式表: `@import "common.wxss";`

### 内联样式
`<text class="article1" style="color: {{textColor}}">`
* 静态样式最好写在 wxss 文件中, 以免影响渲染速度;
* 动态样式写在`style="xxx: {{ yyy }}"`中;