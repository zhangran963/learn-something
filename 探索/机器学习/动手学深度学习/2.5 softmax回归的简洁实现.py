import d2lzh as d2l
from mxnet import gluon, init
from mxnet.gluon import loss as gloss, nn


batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)


# 定义并初始化模型
net = nn.Sequential()
net.add( nn.Dense(10) )
net.initialize( init.Normal(sigma=0.01) )

# softmax 和 交叉熵损失函数
loss = gloss.SoftmaxCrossEntropyLoss()

# 定义优化算法
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.1})

# 训练模型
num_epochs = 15
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, None, None, trainer)

