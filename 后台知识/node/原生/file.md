-   都有同步和异步两种形式;
-   异步形式: 回调中第一项是值 error, 可能是 null 或 undefined;
-   同步形式: 任何异常都会被立即抛出，可以使用 try/catch 来处理异常，或让异常向上冒泡;

## open

-   `fs.open(path, ?flag, ?mode, callback )`: 异步打开;

    -   path: 路径 string / Buffer ;
        -   不能直接读取远程文件;
    -   flag:
        -   `r`: 以读取模式打开文件。如果文件不存在则发生异常
        -   `r+`: 以读写模式打开文件。如果文件不存在则发生异常
        -   `w`: 以写入模式打开文件。文件会被创建（如果文件不存在）或截断（如果文件存在）
        -   [更多](http://nodejs.cn/api/fs.html#fs_fs_open_path_flags_mode_callback)
    -   mode: 只有当文件被创建时才有效。默认为 0o666，可读写
    -   callback: 回调函数, (error, fd),
        -   `fd`: 文件描述符, 类似 ID ?

-   `fs.openSync(path, flags[, mode])`: 打开文件(同步);

### readFile

-   `fs.readFile(path, options?, callback)`: 读取文件;

    -   path: 路径 string / Buffer / 文件描述符 ;
    -   options:
        -   encoding: string 默认 null;
        -   flag: 默认 r;
    -   callbakc: 回调 (error, data)
        -   data: String | Buffer;
        -   `data.toString()`

-   `fs.readFileSync(path[, options])`: 读取文件(同步)

### stat

-   `fs.stat(path, callback)`: 获取文件信息;
    -   path: 路径 string / Buffer ;
    -   callback: 回调(error, data)
        -   data: 信息
            -   `.isFile()`: 判断是否是文件;
            -   `.isDirectory()`: 判断是否目录;
-   `fs.statSync(path[, options])`: 读取信息(同步);

**文件系统**
`var fs = require("fs")`

-   `fs.readFile(url,callBack)`异步读取文件,(err,data),推荐；`fs.readFileSync()`同步读取文件；
-   `fs.open(path, flags[, mode], callback)` 在异步模式下打开文件的语法格式

    > 1.path - 文件的路径。  
    > 2.flags - 文件打开的行为  
    > 3.mode - 设置文件模式(权限)，文件创建默认权限为 0666(可读，可写)。  
    > 4.callback - 回调函数，带有两个参数如：callback(err, fd)。fd 指文件描述符，write 或 read 中可用到

-   `fs.stat(path, callback)`获取文件信息

    > 1.path - 文件路径。  
    > 2.callback - 回调函数，带有两个参数如：(err, stats), stats 是 fs.Stats 对象。

-   `fs.writeFile(filename, data[, options], callback)` 写入文件

    > 1.path - 文件路径。  
    > 2.data - 要写入文件的数据，可以是 String(字符串) 或 Buffer(流) 对象。  
    > 3.options - 该参数是一个对象，包含 {encoding, mode, flag}。默认编码为 utf8, 模式为 0666 ， flag 为 'w'  
    > 4.callback - 回调函数*一定会执行*，回调函数只包含错误信息参数(err)，在写入失败时返回。

-   `fs.read(fd, buffer, offset, length, position, callback)` 异步读取文件**先 open，再 read，再 close**
    > 需新建 buffer 对象,用于存储读取出的数据

> 1.fd - 通过 fs.open() 方法返回的文件描述符。  
> 2.buffer - 数据写入的缓冲区。  
> 3.offset - 缓冲区写入的写入偏移量。  
> 4.length - 要从文件中读取的字节数。
> 5.position - 文件读取的起始位置，如果 position 的值为 null，则会从当前文件指针的位置读取。  
> 6.callback - 回调函数，有三个参数 err, bytesRead, buffer; err 为错误信息， bytesRead 表示读取的字节数，buffer 为缓冲区对象。

-   `fs.close(fd, callback)` 关闭文件

    > 1.callback - 回调函数，没有参数。

-   `fs.ftruncate(fd, len, callback)` 异步模式下截取文件

    > 1.len - 文件内容截取的长度。  
    > 2.callback - 回调函数，有参数 err。

-   `fs.unlink(path, callback)` 删除文件

    > 1.path 文件路径；
    > 2.callback 回调函数，没有参数。

-   `fs.mkdir(path[, mode], callback)` 创建目录

    > 1.path 文件路径；  
    > 2.mode - 设置目录权限，默认为 0777。  
    > 3.callback 回调函数，有参数 err。

-   `fs.readdir(path, callback)` 读取目录

    > 1.path 目录路径；  
    > 2.callback 回调函数，有两个参数 err, files，err 为错误信息，files 为 目录下的文件数组列表。

-   `fs.rmdir(path, callback)` 删除目录
    > 1.path 文件路径；  
    > 2.callback 回调函数，有参数 err。
