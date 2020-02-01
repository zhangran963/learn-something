### 使用 cpulimit 工具

> 受限的内容, 严格不超过限制值运行, 无论资源是否富裕;

1. `apt install cpulimit`: 安装 cpulimit 工具;
2. `cpulimit --limit [最高比例] --pid [PID值] --background`: 启用对某 PID 的限制;

- 示例: `cpulimit --limit 30 --pid 27229 --background`
