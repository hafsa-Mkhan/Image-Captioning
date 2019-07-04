import os
path = 'C:/Users/hmaqsood/Downloads/flicker8k-dataset/Flickr8k_Dataset/Flicker8k_Dataset'
imgList = os.listdir(path)

textFile = open('train2.txt','w')
i=0
for img in imgList:
    imgPath = path+img+'\n'
    textFile.write(img)
    i=i+1
    if(i==6000):
        break;
textFile.close()

f=open("train.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print('Hey')
    print(contents)
