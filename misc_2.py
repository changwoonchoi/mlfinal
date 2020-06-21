import os
import cv2 as cv
import numpy as np
files=os.listdir('./Data/train')

flist=[i for i in files]

for f in files :
    img=cv.imread('./train/'+f)
    img2=np.zeros((64,160,3))
    img2[:60,:,:]=img
    cv.imwrite('./train_new2/'+f,img2)

