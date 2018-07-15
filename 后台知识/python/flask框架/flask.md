### 头部处理
`from flask import Flask` 引入框架
`from flask import request` 引入url处理工具
`app = Flask(__name__)` 定义app, 后面用到

***
### 中间业务函数
```
# 监听对应url,d定义相应的处理方法(get,post,put,delete等)
@app.route("/", methods=["GET","POST"])
def home():
    return '''<h1>Home页 <a href="/signin">登录</h1>'''
```

***
### 尾部处理
```
# 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。
# 开启服务器并设置成debug模式(保存自动重启)
if __name__=="__main__":
    app.run(debug=True)
```
***
### app.route()
* `@app.route("/user/<username>",methods=["get","post"])`定义了变量`username`, 默认是path(字符串)模式;
* `@app.route("/user/<int:person_id>")`定义变量`person_id`, 是整数形式;
* `@app.route("/user/<float:number>")`定义变量`number`, 是浮点数形式;

***
# request
* `request.method`读取请求类型, `GET/POST/DELETE/PUT`等;

***
###  `x is y`和`x==y`的区别
* `is`判断id是否相同;
* `==`仅判断值是否相同;
```
x=y=[1,2,3]
z=[1,2,3]
x is y => True;
x is z => Flase;
x == z => True;
# 若赋值相同的 数字/字符串 时, id值都相等;
```
* `print( id(x) )` 查看x的id值;
