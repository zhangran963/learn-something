### 添加(增)
* `db.member.insert({"name": "四叶草", "age": 27})`: 插入数据, BSON(二进制化的JSON)格式;

### 移除(删)
* `db.member.remove({})`: 移除所有;
* `db.member.remove({"age": 20})`: 移除 age=20 的所有项;
* `db.member.remove({"age": {$lt: 20}})`: 移除 age<20 的所有项;
* `db.member.remove({"age": {$lte: 20}})`: 移除 age<=20 的所有项;
* `db.member.remove({"age": {$gt: 20}})`: 移除 age>20 的所有项;
* `db.member.remove({"age": {$gte: 20}})`: 移除 age>=20 的所有项;
* `db.member.remove({"age": {$ne: 20}})`: 移除 age!=20 的所有项;

### 更新(改)
* `db.member.update({"name": "四叶草","age": 34}, {$set: {"age": 777}})`: 更改 name=四叶草&&age=34 的数据项为 age=777 ;
* `db.member.update({"age": 34}, {$inc: {"age": 6}})`: 更改 age=34 的数据项为 age=40 (age=34+6) ;

### 查询(查)
* 进入某一个数据库后;
* `db.member.find()`: 列出全部数据
* `db.member.find({"name": "四叶草"})`: 查询 name=四叶草 的数据项;
* `db.member.find({"age": {$in: [15,16]}})`: 查询 age=15或 age=16 的数据项;
* `db.member.find({"name": "四叶草"}).count()`: 查询 name=四叶草 的数据项的数量;
* `db.member.find().sort({"age": 1})`: 查询结果 按升序(1)/降序(-1) 排列;
* `db.member.find().limit(5)`: 查询结果的 第1到5条 数据项;
* `db.member.find().skip(3).limit(7)`: 查询结果的 第3到7条 数据项;
* `db.member.find({"age":{$type: 2}})`: 查询 age类型是字符串 的数据项;
    * Double:1
    * String:2
    * Object:3
    * Array:4
    * Binary data: 5
    * ![更多内容](https://upload-images.jianshu.io/upload_images/5832745-4b259a703b51d8c8.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)



### 服务器状态
* `db.serverStatus()`

### 数据库统计信息
* `db.stats()`

