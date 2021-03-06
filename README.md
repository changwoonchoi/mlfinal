# Captcha to Text

## About

This is PyTorch implementation of Cap2TxT, CNN+LSTM+CTC Network for OCR. (Final Project for 2020 Spring ML Class)

[**Paper**](https://github.com/changwoonchoi/mlfinal/blob/master/report/2020Spring_ML_final_2014_17733.pdf)
<a href="/report/2020Spring_ML_final_2014_17733.pdf" class="image fit"><img src="images/marr_pic.jpg" alt=""></a>

## Dependence

- Ubuntu 18.04
- Python 3.7
- torch == 1.3.1
- torchvision ==0.4.2
- numpy
- opencv-python
- lmdb
- jupyterlab

## Installation
 **conda environment setting**

```
conda create -n cap2txt python=3.7
source activate cap2txt
conda install pytorch==1.3.1 torchvision==0.4.2 cudatoolkit=10.0 -c pytorch
pip install -r requirements.txt
```

## Train Network
### File Directory
```
REAME.md
\DATA
  \train
  \test
  \train_prepared
  train.txt
  test.txt
\ckpt
main.ipynb
misc.py
misc_2.py
misc_3.py
utils.py
create_dataset.py
requirements.txt
```

### Prepare Dataset
You can prepare dataset by following the code in main.ipynb.

```
python misc.py
python misc_2.py
python misc_3.p
python create_dataset.py
```



