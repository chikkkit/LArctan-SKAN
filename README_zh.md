# LSS-SKAN

## 声明
这是论文 LArctan-SKAN: Simple and Efficient Single-Parameterized Kolmogorov-Arnold Networks using Learnable Trigonometric Function 中的实验代码，包含**如果你正在寻找用于快速构建SKAN的Python库，点击[这里](https://github.com/chikkkit/SKAN)前往skan库的github仓库。**

## 使用
本代码是在Python3.12.3下运行的。要使用该库代码，请确保安装了如下Python库：
```
numpy==2.1.2
pandas==2.2.3
scikit_learn==1.5.2
single_kan==0.2.0
torch==2.4.1+cu121
torchvision==0.19.1+cu121
tqdm==4.66.4
```
然后执行脚本运行代码：
```
python LArctan_SKAN_30epoch_lr000101.py
```
这将运行文章的实验。请注意，该库只包含LSS-SKAN，LSin-SKAN，LCos-SKAN和LArctan-SKAN库的代码。其他网络的代码见github库[LSS-SKAN](https://github.com/chikkkit/LSS-SKAN)的[LSS_SKAN_30epoch_lr000101.py](https://github.com/chikkkit/LSS-SKAN/blob/main/LSS_SKAN_30epoch_lr000101.py)文件。

## 参考文献
[1] LArctan-SKAN: Simple and Efficient Single-Parameterized Kolmogorov-Arnold Networks using Learnable Trigonometric Function 
