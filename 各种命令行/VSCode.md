### 打开 vscode 命令模式
1. `shift + cmd + p`打开 vscode 命令模式;
2. `quit`退出;

### 打开文件
1. `cmd + p`: 打开命令模式;
2. 自由输入文件名;
3. `文件名 + #行数`: 转到某文件的某行;


### 终端
1. `ctrl + '`: 显示/隐藏终端;
2. `ctrl + d`: 关闭终端;
### 终端位置
1. `查看>外观>切换面板位置`: 终端窗口切换为 右侧/底部 显示;


***
***

### 编辑中
`cmd + o` 打开文件夹;
`cmd + w` 关闭当前文件;
`cmd + enter`: 另起一行;


### 缩进4格
1. 设置 tab 不生效的处理
```
"editor.detectIndentation": false,
```

2. 格式化.vue中的 `<style>` 和 `<script>` 片段;
```
"beautify.language": {
    "js": {
        "type": [
            "javascript",
            "json",
            "jsonc"
        ],
        "filename": [
            ".jshintrc",
            ".jsbeautifyrc"
        ]
    },
    "css": [
        "css",
        "scss",
        "less"
    ],
    "html": [
        "htm",
        "html",
        "vue"
    ]
}
```



### 优秀插件
* `Prettier-Code formatter`: 格式化 JSX 语法;



### 格式化
* `shift + option + F`: 格式化文件