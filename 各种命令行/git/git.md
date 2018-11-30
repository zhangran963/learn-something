### 查看状态 
* `git status ` 

### 加入文件
* `git add [文件路径]`

### 全部加入
* `git add .`

### 提交 P
* `git commit -m [描述内容]`
* `git reset --soft HEAD^`撤销 commit, 保留代码;

### 缓存进行中的文件
* `git stash`缓存;
* `git stash pop`弹出并删除列表中弹出的项;
* `git stash apply`弹出不删除列表中的项; `git stash drop`手动删除列表项;
* `git stash apply stash@{0}`恢复指定的缓存项;


### 查看历史纪录
* `git log` 查看历史纪录;
* `git log --pretty=oneline` 单行打印历史纪录;
* `git reflog` 查看所有历史纪录(包含被删除的 commit);



### 再返回回退前
* `git reset --hard [回退前版本的前几个字母]`, 返回回退前状态,需要知道回退前的 id;
    * 若不知道 id 了, 通过`git reflog`再次查找;


### 撤销修改
* `git checkout -- [文件路径]`撤销文件的修改,返回到最近一次 修改后 或 add后 的状态;
    * 注: `--`不能缺失;
    * 本质是用版本库的内容替换工作区的修改;
* 若已经 add后(暂存区) 用`git reset HEAD file`把文件重新放回工作区;

### 删除文件
* `git rm [文件路径]` 删除一个文件;
* `git checkout -- `


### 修复 bug 过程
1. 先把手里的工作缓存`git stash`; 可查看缓存`git stash list`;
2. 创建新分支并切换到此分支 `git checkout -b bug01`;
3. bug01的分支: 修改 bug中;
4. bug01的分支: `git add xxx`, `git commit -m "修改了 bug01 "`;
5. 返回原分支 `git checkout 原分支`;
6. 合并 bug01 的内容`git merge --no-ff -m "合并的说明" bug01`;
7. 把缓存的内容弹出来`git stash pop`(同时删除缓存列表对性项);
8. 可能有合并的问题处理掉;





### 创建新分支
1. `git branch xxx` 创建名为xxx的分支；
2. `git checkout xxx` 切换到分支 xxx;
3. `git checkout -b xxx` 创建并切换到 xxx;
4. `git merge xxx` 合并“其他分支”到当前分支;
5. `git branch`查看当前分支;

### 合并分支
* 一般在 `master` 分支上操作;
* `git merge xxx` 把 xxx 分支合并到 当前分支 上

### 删除旧分支
* `git branch -d xxx`把没用的分支删除掉;


### 查看合并信息
* `git log --graph --pretty=oneline --abbrev-commit`;
* `git log --graph` 查看分支合并图;

### Fast forward 模式
合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。

* 默认采用 fast forward 模式, 直接指针移动到合并完成处;
* 禁用 fast forward 模式, 合并时生成一个新的 commit, `git merge --no-ff -m "禁用 fast forward 模式" dev`;


### 多人合作开发
* 本地新建的分支如果不推送到远程，对其他人就是不可见的；
* 从本地推送分支，使用`git push origin branch-name`，如果推送失败，先用`git pull`抓取远程的新提交；
* 在本地创建和远程分支对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；
* 建立本地分支和远程分支的关联，使用`git branch --set-upstream branch-name origin/branch-name`；
* 从远程抓取分支，使用`git pull`，如果有冲突，要先处理冲突。


### 撤销合并
1. `git checkout 分支名`先切换到分支名;
2. `git reset --merge`撤销合并;

`git merge --abort`取消合并;

### 清除本地
* `git clean -df`: 清除本地未提交的更改;
* `git reset --hard`: 清除本地已提交的更改;


### rebase 模式合并
* 普通合并用 merge 形式, 有分支;
* rebase 合并能做成不带分支的形式;
1. `git checkout -b 开发分支 master`: 在 master上分出自己的开发分支;
2. 开发分支上做了修改;
3. 开发分支上修改完后, master 分支上也被别人做了修改了;
4. `git checkout 开发分支`: 在开发分支上;
5. `git rebase master`: 把 master 上最新的内容加到开发分支前;
    * 这些命令会把你的"mywork"分支里的每个提交(commit)取消掉，并且把它们临时 保存为补丁(patch)(这些补丁放到".git/rebase"目录中),然后把"mywork"分支更新 为最新的"origin"分支，最后把保存的这些补丁应用到"mywork"分支上。

### rebase 冲突
* rebase 合并也会产生冲突;
1. 产生冲突后, rebase过程停止, 等待解决冲突;
2. 解决完冲突;
3. `git-add`: 更新这些内容的索引;
4. `git rebase --continue`: 继续合并;
* `git rebase --abort`: 在任何时候，你可以用--abort参数来终止rebase的行动，并且"mywork" 分支会回到rebase开始前的状态。


***
***





### 上传
1. `git add xxx` 先保存(缓存);
2. `git commit -m "说明文字"`给本次上传添加说明;
3. `git push origin master` 把内容传到远程仓库;
3. `git push -u origin master`把本地库的内容推送到远程;

### 下载
1. `git pull --rebase origin master`获取远程库与本地同步合并（如果远程库不为空必须做这一步，否则后面的提交会失败）


