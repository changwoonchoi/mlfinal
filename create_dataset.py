import os
import lmdb
import cv2
import numpy as np
import argparse
import shutil
import sys

def checkImageIsValid(imageBin):
    if imageBin is None:
        return False

    try:
        imageBuf = np.fromstring(imageBin, dtype=np.uint8)
        img = cv2.imdecode(imageBuf, cv2.IMREAD_GRAYSCALE)
        imgH, imgW = img.shape[0], img.shape[1]
    except:
        return False
    else:
        if imgH * imgW == 0:
            return False

    return True


def writeCache(env, cache):
    with env.begin(write=True) as txn:
        for k, v in cache.items():
            if type(k) == str:
                k = k.encode()
            if type(v) == str:
                v = v.encode()
            txn.put(k,v)

def createDataset(outputPath, imagePathList, labelList, lexiconList=None, checkValid=True):
   
    if os.path.exists(outputPath):
        shutil.rmtree(outputPath)
        os.makedirs(outputPath)
    else:
        os.makedirs(outputPath)

    assert (len(imagePathList) == len(labelList))
    nSamples = len(imagePathList)
    env = lmdb.open(outputPath, map_size=1099511627776)
    cache = {}
    cnt = 1
    for i in range(nSamples):
        imagePath = imagePathList[i]
        label = labelList[i]

        if not os.path.exists(imagePath):
            print('%s does not exist' % imagePath)
            continue
        with open(imagePath, 'rb') as f:
            imageBin = f.read()
        if checkValid:
            if not checkImageIsValid(imageBin):
                print('%s is not a valid image' % imagePath)
                continue

        imageKey = 'image-%09d' % cnt
        labelKey = 'label-%09d' % cnt
        cache[imageKey] = imageBin
        cache[labelKey] = label
        if lexiconList:
            lexiconKey = 'lexicon-%09d' % cnt
            cache[lexiconKey] = ' '.join(lexiconList[i])
        if cnt % 1000 == 0:
            writeCache(env, cache)
            cache = {}
        cnt += 1
    nSamples = cnt-1
    cache['num-samples'] = str(nSamples)
    writeCache(env, cache)
    env.close()

def read_data_from_folder(folder_path):
    image_path_list = []
    label_list = []
    pics = os.listdir(folder_path)
    pics.sort(key = lambda i: len(i))
    for pic in pics:
        image_path_list.append(folder_path + '/' + pic)
        label_list.append(pic.split('_')[0])
    return image_path_list, label_list

def read_data_from_file(file_path):
    image_path_list = []
    label_list = []
    f = open(file_path)
    while True:
        line1 = f.readline()
        line2 = f.readline()
        if not line1 or not line2:
            break
        line1 = line1.replace('\r', '').replace('\n', '')
        line2 = line2.replace('\r', '').replace('\n', '')
        image_path_list.append(line1)
        label_list.append(line2)

    return image_path_list, label_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type = str, required = True, help = 'lmdb data output path')
    parser.add_argument('--folder', type = str, help = 'path to folder which contains the images')
    parser.add_argument('--file', type = str, help = 'path to file which contains the image path and label')
    args = parser.parse_args()

    if args.file is not None:
        image_path_list, label_list = read_data_from_file(args.file)
        createDataset(args.out, image_path_list, label_list)
        #show_demo(2, image_path_list, label_list)
    elif args.folder is not None:
        image_path_list, label_list = read_data_from_folder(args.folder)
        createDataset(args.out, image_path_list, label_list)
        #show_demo(2, image_path_list, label_list)
    else:
        print ('Please use --floder or --file to assign the input. Use -h to see more.')
        sys.exit()
