### 存储库(oss)注意事项

1. "读写权限"可以设置成`公共读`, 写入安全, 读取方便;
2. 绑定用户域名后, 可以方便地写 url;

---

### 阿里云 OSS 对象存储配合域名证书等

1. 购买 OSS 对象存储, 获取此对象存储的域名, 如`databasing.oss-cn-beijing.aliyuncs.com`;
2. 设置对象存储的 语义化域名, 如`cdn.thesoundofsilence.top`;
   ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200131200349.png)
3. 设置语义化的域名, 指向 对象存储的域名;
   ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200131200129.png)
4. 申请语义化域名的证书, 下载留存
   ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200131200620.png)
5. 在 OSS 对象存储 > 域名管理 > 证书托管 中, 设置证书 pem 和 key, 保存, 即可生效;
   ![](https://databasing.oss-cn-beijing.aliyuncs.com/markdown/20200131201236.png)
