import d2lzh as d2l
from mxnet import autograd, nd

# 获取读取数据
batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

# 初始化模型参数
num_inputs = 784
num_outputs = 10

W = nd.random.normal(scale=0.01, shape=(num_inputs, num_outputs))
b = nd.zeros(num_outputs)

# 梯度
W.attach_grad()
b.attach_grad()

### softmax运算
def softmax(X):
    X_exp = X.exp()
    return X_exp/X_exp.sum(axis=1, keepdims=True)

### 模型
def net(X):
    return softmax(nd.dot(X.reshape(-1, num_inputs), W)+b)

### 损失函数
def cross_entropy(y_hat, y):
    return - nd.pick(y_hat, y).log()

### 准确率函数(优化函数)
def evaluate_accuracy(data_iter, net):
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
        y = y.astype('float32')
        acc_sum += (net(X).argmax(axis=1) == y).sum().asscalar()
        n += y.size
    
    # 数据集的准确率
    return acc_sum / n



### 训练
num_epochs = 15
lr = 0.1
printt = True
def train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size,params=None, lr=None, trainer=None):
    
    global printt

    for epoch in range(num_epochs):
        # 每一次训练
        train_l_sum = 0.0
        train_acc_sum = 0.0
        n = 0

        # 小批量数据
        for X,y in train_iter:
            # 某一次训练
            with autograd.record():
                # 某一数据的训练预测值列表
                
                y_hat = net(X)
                l = loss(y_hat, y).sum()
                # if printt:
                    
                #     print(y_hat[0].sum())
                #     printt = False

            l.backward()

            if trainer is None:
                d2l.sgd(params, lr, batch_size)
            else:
                trainer.step(batch_size)
            
            y = y.astype('float32')
            train_l_sum += l.asscalar()
            train_acc_sum += (y_hat.argmax(axis=1) == y).sum().asscalar()
            n += y.size

        # 对测试数据求准确率
        test_acc = evaluate_accuracy(test_iter, net)

        print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f'
              % (epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))

train_ch3(net, train_iter, test_iter, cross_entropy, num_epochs, batch_size, [W,b], lr)
