import cv2
import glob

path = '/home/adventum/Desktop/OCTS/color usable oct/*.*'   
files=glob.glob(path) 

import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

files.sort(key=natural_keys)

i=0
for file in files:
    #print(file)
    img = cv2.imread(file,0)
    cv2.imwrite('/home/adventum/Desktop/OCTS/blk/gray'+str(i)+'.jpg',img)
    i+=1


