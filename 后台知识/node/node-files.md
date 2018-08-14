* 都有同步和异步两种形式;
* 异步形式: 回调中第一项是值 error, 可能是 null 或 undefined;
* 同步形式: 任何异常都会被立即抛出，可以使用 try/catch 来处理异常，或让异常向上冒泡;


## open
* `fs.open(path, ?flag, ?mode, callback )`: 异步打开;
    * path: 路径 string / Buffer ;
        * 不能直接读取远程文件;
    * flag:
        * `r`: 以读取模式打开文件。如果文件不存在则发生异常
        * `r+`: 以读写模式打开文件。如果文件不存在则发生异常
        * `w`: 以写入模式打开文件。文件会被创建（如果文件不存在）或截断（如果文件存在）
        * [更多](http://nodejs.cn/api/fs.html#fs_fs_open_path_flags_mode_callback)
    * mode: 只有当文件被创建时才有效。默认为 0o666，可读写
    * callback: 回调函数, (error, fd),
        * `fd`: 文件描述符, 类似 ID ?

* `fs.openSync(path, flags[, mode])`: 打开文件(同步);

### readFile
* `fs.readFile(path, options?, callback)`: 读取文件;
    * path: 路径 string / Buffer / 文件描述符 ;
    * options:
        * encoding: string 默认 null;
        * flag: 默认 r;
    * callbakc: 回调 (error, data)
        * data: String | Buffer;
        * `data.toString()`

* `fs.readFileSync(path[, options])`: 读取文件(同步)


### stat
* `fs.stat(path, callback)`: 获取文件信息;
    * path: 路径 string / Buffer ;
    * callback: 回调(error, data)
        * data: 信息
            * `.isFile()`: 判断是否是文件;
            * `.isDirectory()`: 判断是否目录;
* `fs.statSync(path[, options])`: 读取信息(同步);