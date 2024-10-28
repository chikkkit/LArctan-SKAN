# LSS-SKAN
<p align="center"><b>English</b> / <a href="https://github.com/chikkkit/LArctan-SKAN/blob/main/README_zh.md">简体中文</a></p>

## Introduction
This repository contains the experimental code for the paper ["LArctan-SKAN: Simple and Efficient Single-Parameterized Kolmogorov-Arnold Networks using Learnable Trigonometric Function."](https://arxiv.org/abs/2410.14951) [1] **If you are looking for a Python library to quickly build SKANs, please click [here](https://github.com/chikkkit/SKAN) to visit the SKAN GitHub repository.**


## Usage
This code runs on Python 3.12.3. To use the library, ensure that the following Python packages are installed:


```python
numpy==2.1.2
pandas==2.2.3
scikit_learn==1.5.2
single_kan==0.2.0
torch==2.4.1+cu121
torchvision==0.19.1+cu121
tqdm==4.66.4
```

To execute the experiment in the paper, run the following script:

```bash
python LArctan_SKAN_30epoch_lr000101.py
```
This will run the experimental setup described in the paper. Note that this repository only includes code for the LSS-SKAN, LSin-SKAN, LCos-SKAN, and LArctan-SKAN networks. For other networks, refer to the GitHub repository [LSS-SKAN](https://github.com/chikkkit/LSS-SKAN) and the file [LSS_SKAN_30epoch_lr000101.py](https://github.com/chikkkit/LSS-SKAN/blob/main/LSS_SKAN_30epoch_lr000101.py).


## References
[1] Z. Chen and X. Zhang, “LSS-SKAN: Efficient Kolmogorov-Arnold Networks based on Single-Parameterized Function,” Oct. 19, 2024, arXiv: arXiv:2410.14951. doi: 10.48550/arXiv.2410.14951.
