[git bisect](http://www.ruanyifeng.com/blog/2018/12/git-bisect.html)


### 查找bug出现的位置
将代码提交的历史，按照两分法不断缩小定位。
1. `git bisect start [终点] [起点]`: 开始查找位置
   * 示例: git bisect start HEAD a1b2c3d4, 从a1b2c3d4处查找到最新内容;
2. 验证是否合格
3. 两种可能, 分别输入`git bisect good` 或 `git bisect bad`, 继续二分法查找, 直到查到具体的提交;
4. 阅读代码, 查看错误原因(未修改);
5. 退出bisect模式, 回到最近的提交;
6. 改bug;
7. ...