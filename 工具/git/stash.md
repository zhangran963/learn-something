### 保存
* `git stash`: 保存当前的全部文件(不包含未跟踪文件);
* `git stash save '名称'`: 保存当前文件并命名;


### 查看
* `git stash list`: 查看保存的列表
![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200131161435.png)
* `git stash show`: 查看保存的文件
![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200131161627.png)


### 释放并删除
* `git stash pop`: 弹出并删除所有项;
* `git stash apply`: 仅弹出所有项; 

* `git stash pop stash@{0}`: 弹出并删除指定项
* `git stash apply stash@{0}`: 仅弹出指定项


### 删除
* `git stash drop`: 手动删除列表项;

