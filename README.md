# LSS-SKAN

## Notice
This repository contains the experimental code for the paper *LArctan-SKAN: Simple and Efficient Single-Parameterized Kolmogorov-Arnold Networks using Learnable Trigonometric Function*. **If you're looking for a Python library to quickly build SKAN, please visit the [SKAN library GitHub repository](https://github.com/chikkkit/SKAN).**

## Usage
This code is designed to run on Python 3.12.3. To use this repository, make sure you have the following Python libraries installed:
```
numpy==2.1.2
pandas==2.2.3
scikit_learn==1.5.2
single_kan==0.2.0
torch==2.4.1+cu121
torchvision==0.19.1+cu121
tqdm==4.66.4
```
Then, run the code by executing the following script:
```
python LArctan_SKAN_30epoch_lr000101.py
```
This will initiate the experiment as described in the paper. Please note that the experimental results can vary depending on the hardware specifications, particularly the GPU memory size.
