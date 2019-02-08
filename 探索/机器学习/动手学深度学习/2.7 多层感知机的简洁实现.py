### 多层感知机的简洁实现

import d2lzh as d2l
from mxnet import gluon, init
from mxnet.gluon import loss as gloss,nn

### 用'层容器'连接多个层
net = nn.Sequential()
net.add(nn.Dense(256, activation='relu'), nn.Dense(10))
net.initialize(init.Normal(sigma=0.01))

### 数据
batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

### 损失函数
loss = gloss.SoftmaxCrossEntropyLoss()

trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.5})

### 训练
num_epochs = 5
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, None, None, trainer)