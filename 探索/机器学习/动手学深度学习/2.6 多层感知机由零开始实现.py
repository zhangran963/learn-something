### 多层感知机由零开始实现

import d2lzh as d2l
from mxnet import nd
from mxnet.gluon import loss as gloss


batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

num_inputs = 784
num_outputs = 10
num_hiddens = 256

### 初始化(两套参数)
W1 = nd.random.normal(scale=0.01, shape=(num_inputs, num_hiddens))
b1 = nd.zeros(num_hiddens)
W2 = nd.random.normal(scale=0.01, shape=(num_hiddens, num_outputs))
b2 = nd.zeros(num_outputs)
params = [W1,b1,W2,b2]
for param in params:
        param.attach_grad()


### 激活函数
def relu(X):
    return nd.maximum(X,0)


### 模型函数
# 传到下一层之前, 先用激活函数处理一下
def net(X):
        X = X.reshape((-1, num_inputs))
        H = relu(nd.dot(X,W1)+b1)
        return nd.dot(H,W2)+b2

### 损失函数
loss = gloss.SoftmaxCrossEntropyLoss()


### 训练
num_epochs = 15
lr = 0.5
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, params, lr)


