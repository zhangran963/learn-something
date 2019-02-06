from mxnet import autograd, nd

num_inputs = 2  # 特征数量
num_examples = 1000  # 样本数量
true_w = [2,-3.4]  # 真实值w
true_b = 4.2 # 真实值b
# x1,x2 数据集
features = nd.random.normal(scale=1, shape=(num_examples, num_inputs))
# y 数据集
labels = nd.dot(features, nd.array(true_w).T) + true_b
labels += nd.random.normal(scale=0.01, shape=labels.shape)


### 分组(小数据集)提供数据
from mxnet.gluon import data as gdata
batch_size = 10
# 关联数据(按顺序)
dataset = gdata.ArrayDataset(features, labels)
# 生成小数据集函数
# 数据 / 大小 / 是否打乱顺序
data_iter = gdata.DataLoader(dataset, batch_size, shuffle=True)

### 定义模型
from mxnet.gluon import nn
# 串联各个层的容器
net = nn.Sequential()
# 全连接层是一个 Dense 的实例, 并定义输出个数为1
net.add(nn.Dense(1))

### 初始化参数 w b
from mxnet import init
net.initialize(init.Normal(sigma=0.01))

### 损失函数
from mxnet.gluon import loss as gloss
# L2范数损失(平方损失)
loss = gloss.L2Loss()

### 优化算法
from mxnet import gluon
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.03})

### 开始训练
# 全部数据集训练 n 次
num_epochs = 3
for epoch in range(num_epochs):
    for X,y in data_iter:
        with autograd.record():
            l = loss(net(X), y)
        # 求梯度
        l.backward()
        # 修正 w,b
        trainer.step(batch_size)

    # 全部数据完成一次后 
    l = loss(net(features), labels)
    print('epoch %d, loss: %f' % (epoch, l.mean().asnumpy()))


### 查看结果
dense = net[0]
print( dense.weight.data() )
print( dense.bias.data() )