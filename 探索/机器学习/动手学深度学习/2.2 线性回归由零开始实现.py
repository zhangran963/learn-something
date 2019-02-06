# %matplotlib inline
from IPython import display
from matplotlib import pyplot as plt
from mxnet import autograd, nd
import random


num_inputs = 2  # 特征项数
num_examples = 1000  # 训练集数
true_w = [2,-3.4]
true_b = 4.2
features = nd.random.normal(scale=1, shape=(num_examples, num_inputs))
# print( features )

# 生成 公式
labels = nd.dot(features, nd.array(true_w).T) + true_b
# 加入 噪声
labels += nd.random.normal(scale=0.01, shape=labels.shape)


# batch_size 数据间隔
# 隔指定间隔后, 返回一组数据;
def data_iter(batch_size, features, labels):
    # 数据
    num_examples = len(features)
    # 0-999顺序组成的数组
    indices = list(range(num_examples))
    # 打乱顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        # i: 0,10,20,...,990
        j = nd.array( indices[i: min(i + batch_size, num_examples)] )
        # j: 10项索引组成一个数组, 共产生100次;
        
        yield features.take(j), labels.take(j)  # take函数根据索引返回对应元素
    
batch_size = 10

# 初始化参数
w = nd.random.normal(scale=0.01, shape=(num_inputs, 1))
b = nd.zeros(shape=(1,))
# 申请存储梯度所需要的内存
w.attach_grad()
b.attach_grad()

# 模型函数
def linreg(X,w,b):
    return nd.dot(X,w)+b

# 损失函数
# y_hat: 预测值(用暂时预测参数获得)
# y: 真实值(用真实参数获得)
def squared_loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape))**2 / 2

# 优化算法: 处理随机梯度下降的算法
# params
# lr: 学习率
# batch_size: 小批量样本数量
def sgd(params, lr, batch_size):
    for param in params:
        param[:] = param - lr * param.grad / batch_size


## 训练
lr = 0.03  # 学习率
num_epochs = 3  # 迭代周期
net = linreg  # 模型函数
loss = squared_loss  # 损失函数

for epoch in range(num_epochs):  # 把全部训练数据训练 num_epochs 次
    # 在每一个迭代周期中，会使用全部训练数据,分成相等份额,把所有样本训练一次（假设样本数能够被批量大小整除）
    # X和y分别是小批量样本的特征和标签
    for X, y in data_iter(batch_size, features, labels):
        # 记录和求梯度有关的计算
        with autograd.record():
            l = loss(net(X, w, b), y)  # l是有关X和y的损失
        l.backward()  # 损失对模型参数求梯度(在优化算法中使用/读取)

        sgd([w, b], lr, batch_size)  # 随机梯度下降迭代模型参数(调整参数)
    
    train_l = loss(net(features, w, b), labels)
    # 索引 , 均值.转换np格式
    print('epoch %d, loss %f' % (epoch + 1, train_l.mean().asnumpy()))

# 参数对比
# print(true_w, w)
# print(true_b, b)
