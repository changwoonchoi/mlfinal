import os
import cv2 as cv
import numpy as np
files=os.listdir('./Data/train')

flist=[i for i in files]

for f in files :
    os.rename('./Data/train/'+f,('./Data/train/'+f)[:-4])
