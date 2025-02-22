import tqdm
import torchvision
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import time
from sklearn.metrics import f1_score
import numpy as np
import pandas as pd
from skan import SKANNetwork

# 定义自定义基函数
def lsin(x, k):
    return k * torch.sin(x)

def lcos(x, k):
    return k * torch.cos(x)

def larctan(x, k):
    return k * torch.atan(x)

def lshifted_softplus(x, k):
    return torch.log(1 + torch.exp(k*x)) - np.log(2)

# 使用MNIST数据集
transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Lambda(lambda x: x.view(-1))
])
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

res_name = time.asctime().replace(' ', '_').replace(':', '_') + ' Result.csv'

# 单参数非线性函数
lfuns = ['lsin', 'lcos', 'larctan', 'lshifted_softplus']

# 测试这些单变量函数的效果，并将结果保存在dataframe中
res = None

# 计算网络的参数量
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
for lr in [*np.linspace(0.001, 0.01, 10), *np.linspace(0.0001, 0.0009, 9)]:
    for lfun in lfuns:
        if lfun == 'MLP':
            net = nn.Sequential(
                nn.Linear(784, 100),
                nn.ReLU(),
                nn.Linear(100, 10)
            ).to(device)
        else:
            net = SKANNetwork([784, 100, 10], basis_function=eval(lfun)).to(device)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(net.parameters(), lr=lr)
        train_loss = []
        train_accuracy = []
        test_loss = []
        test_accuracy = []
        F1s = []
        for epoch in tqdm.trange(30):
            net.train()
            # 记录训练的时间
            start_time = time.time()
            for x, y in train_loader:
                x = x.to(device)
                y = y.to(device)
                optimizer.zero_grad()
                y_pred = net(x)
                loss = criterion(y_pred, y)
                loss.backward()
                optimizer.step()
            end_time = time.time()
            # 计算训练集上的准确率和损失
            net.eval()
            correct = 0
            total = 0
            loss = 0
            with torch.no_grad():
                for x, y in train_loader:
                    x = x.to(device)
                    y = y.to(device)
                    y_pred = net(x)
                    loss += criterion(y_pred, y).item()
                    _, predicted = torch.max(y_pred.data, 1)
                    total += y.size(0)
                    correct += (predicted == y).sum().item()
            train_loss.append(loss / len(train_loader))
            train_accuracy.append(correct / total)
            # 计算测试集上的准确率和损失
            net.eval()
            correct = 0
            total = 0
            loss = 0
            reals = []
            preds = []
            with torch.no_grad():
                for x, y in test_loader:
                    x = x.to(device)
                    y = y.to(device)
                    y_pred = net(x)
                    loss += criterion(y_pred, y).item()
                    _, predicted = torch.max(y_pred.data, 1)
                    total += y.size(0)
                    correct += (predicted == y).sum().item()
                    reals.extend(y.cpu().numpy())
                    preds.extend(predicted.cpu().numpy())
            F1 = f1_score(reals, preds, average='macro')
            test_loss.append(loss / len(test_loader))
            test_accuracy.append(correct / total)
            param_num = count_parameters(net)
            if res is not None:
                res = res.reset_index(drop=True)
                res = pd.concat([res, pd.DataFrame({'function/KAN type': lfun, 'epoch': epoch, 'lr': lr, 'train loss': train_loss[-1], 
                                                    'train accuracy': train_accuracy[-1], 'test loss': test_loss[-1], 
                                                    'test accuracy': test_accuracy[-1], 'F1': F1, 'run time': round(end_time - start_time, 4),
                                                    'param num': param_num}, index=[-1])], axis=0)
            else:
                res = pd.DataFrame({'function/KAN type': lfun, 'epoch': epoch, 'lr': lr, 'train loss': train_loss[-1], 
                                    'train accuracy': train_accuracy[-1], 'test loss': test_loss[-1], 
                                    'test accuracy': test_accuracy[-1], 'F1': F1, 'run time': round(end_time - start_time, 4),
                                    'param num': param_num}, index=[-1])
            res.to_csv('./result/' + res_name, index=False)