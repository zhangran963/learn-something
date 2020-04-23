### 需求: 左侧固定, 右侧自适应
```scss
.box{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;


  .left{
    width: 100px;
    height: 100px;
  }

  .right{
    flex: 1;

    /**
     * 问题: 右侧自适应宽度时, 若设置过单行省略(white-space: nowrap;)行文本过长时, 会横向撑开;
     * 修复方法:
     * 方法1. width: 0; 加width属性限制宽度, 数值不重要(flex优先级高于width);
     * 方法2. overflow: hidden;
     */
    // width: 0px;
    // overflow: hidden;
  }
}
```