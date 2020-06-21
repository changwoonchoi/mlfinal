import os

path = './Data/train/'
gt='./Data/train.txt'

lineList=list()
with open (gt) as f:
    for line in f:
        lineList.append(line.rstrip('\n'))

for i in range(10000):
    os.rename(path+str(i)+'.png',path+lineList[i]+'.jpg')


