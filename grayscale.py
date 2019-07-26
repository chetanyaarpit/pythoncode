dimport cv2
from PIL import Image
import numpy as np
import glob
import skimage
import cv2
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import glob

#to remove artifacts from the images and change their size.
path = '/media/adventum/C0C5-3B92/To_Chaitanya/normal/*.*'

files=glob.glob(path)
'''
new2 = ""
# traverse in the string  
for y in files:
    new2 += y+'~'

new2 = new2.replace('/media/adventum/C0C5-3B92/To_Chaitanya/Defect/','')
new2 = list(new2.split("~"))
new2.pop()
'''
z=1
for file in files:
    m = cv2.imread(file)
    #print(m)
    for t in range(m.shape[0]):

        for y in range(m.shape[1]):

            if m[t,y][0]!=0:

                   pass

            if m[t,y][0]!=0:

                m[t,y][1]=m[t,y][0]

            if m[t,y][0]!=0:

                m[t,y][2]=m[t,y][0]
    
    m = cv2.resize(m,(1024,1024))
    cv2.imwrite('/media/adventum/C0C5-3B92/To_Chaitanya/normal2/test'+str(z)+'.png',m)
    z = z+1
    
'''
path = '/home/adventum/Documents/new_denoised_trshCairo_Original_resized/*.*'

files=glob.glob(path)

c=0
for file in files:
    m = cv2.imread(file)
    for t in range(m.shape[0]):
        for y in range(m.shape[1]):
            if m[t,y][0]==m[t,y][1]==m[t,y][2]:
                m[t,y][0]=0
                m[t,y][1]=0
                m[t,y][2]=0
    cv2.imwrite('/home/adventum/Documents/allblack/'+str(c)+'.png',m)
    c=c+1
'''