### 安装
> 1. `wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-amazon2-4.0.0.tgz` 下载 mongodb 压缩文件;
2. `tar -xzvf 压缩文件名` 解压;
3. 运行



`db.dropDatabase()` 删除数据库

show dbs //显示数据库
show collections  //显示当前数据库的集合


**启动**
> `mongod --dbpath e:\data\db`
> `/usr/local/Cellar/mongodb/4.0.0/bin/mongod --dbpath /Users/ran/Public/data` 执行 mongodb 文件夹下的命令, 指定数据库存在的文件夹

载入数据文件
> `mongoimport --db test --collection restaurants --drop --file primer-dataset.json`

### 配合使用1 路由
```js
var router = express.Router();
router.get("/",function(req,res){
   res.render("index",{title:"主页index",title2:"我是title2"});
});1
```

### 数据库读取
```js
var mongodb = require("mongodb").MongoClient;
mongodb.connect("mongodb://localhost:27017/ran",function(err,db){
   app.get()
   app.route("/").get(fun).post(fun)

   app.listen(3000);
});
```

### bodyParser
```js
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
```


调试工具
> `assert.equal(真实值,期望值,"不相等时输出的话")` ,插在语句之间，相等时就可忽略，不相等时就报错，显示预置的话；

数据处理
1. db.collection.drop(); 删除集合；
2. db.createCollection(name,[options]); 创建集合
2. db.dropDatabase(); 删除当前库

`db.collectionname.insert({xxxxx:xxxxx})`;
> 插入数据

### 列出数据
* `db.集合名.find()`


`db.mycol.find({},{"title":0,_id:0})`
> 按条目查找显示,0代指"不显示",1代指"显示";

`.skip(num)` 从哪一行开始(默认0)
`db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)`

排序,1指升序,-1指降序
> `db.COLLECTION_NAME.find().sort({KEY:1})`

创建索引
> `db.mycol.ensureIndex({"title":1})`  key 是想创建索引的字段名称，1 代表按升序排列字段值。-1 代表按降序排列。

**指定查询条件**
1. `var cursor =db.collection('restaurants').find( { "borough": "Manhattan" } );`
2. `var cursor =db.collection('restaurants').find( { "address.zipcode": "10075" } );` 属性或嵌套的属性
3. `var cursor =db.collection('restaurants').find( { "grades.score": { $gt: 30 } } );`指定运算符，大于小于
4. and关系
```js
var cursor =db.collection('restaurants').find(
  { "cuisine": "Italian", "address.zipcode": "10075" }
);
```
5. or关系
```js
var cursor =db.collection('restaurants').find(
  { $or: [ { "cuisine": "Italian" }, { "address.zipcode": "10075" } ] }
);
```
6. 排序,1代表升序,-1代表降序
```js
var cursor =db.collection('restaurants').find().sort( { "borough": 1, "address.zipcode": 1 } );
```
