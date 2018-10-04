### 插入并保存数据

```py
# 插入一条数据
collection.insert_one({
    "username": "呵呵"
})

# 插入多条数据
collection.insert_many([{
    "username": "名称1"
}, {
    "username": "名称2"
}])

# 获取游标, 获取全部数据
cursor = collection.find()
for x in cursor:
    print(x)


# 获取单条数据, 默认获取第一条
result = collection.find_one()
# 获取指定条件的单条数据
result = collection.find_one({"age": 18})
print(result)
```


### 更新数据
```py
# 更新*一条*数据
collection.update_one({
    "username": "呵呵"
}, {
    "$set": {"username": "ccc"}
})

# 更新所有符合条件的数据
collection.update_many({
    "username": "呵呵"
}, {
    "$set": {"username": "ccc"}
})

cursor = collection.find()
for x in cursor:
    print(x)
```

### 删除数据
```py
collection.delete_one()


```