* 都有同步和异步两种形式;
* 异步形式: 回调中第一项是值 error, 可能是 null 或 undefined;
* 同步形式: 任何异常都会被立即抛出，可以使用 try/catch 来处理异常，或让异常向上冒泡;


## 打开
* `fs.open(path, ?flag, ?mode, callback )`: 异步打开;
    * path: 路径 string / Buffer / URL;
    * flag:
        * `r`: 以读取模式打开文件。如果文件不存在则发生异常
        * `r+`: 以读写模式打开文件。如果文件不存在则发生异常
        * `w`: 以写入模式打开文件。文件会被创建（如果文件不存在）或截断（如果文件存在）
        * [更多](http://nodejs.cn/api/fs.html#fs_fs_open_path_flags_mode_callback)
    * mode: 只有当文件被创建时才有效。默认为 0o666，可读写
    * callback: 回调函数, (error, fd),
        * `fd`: 文件描述符, 类似 ID ?