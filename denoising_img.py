import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob

path = '/home/adventum/Cairo_Data_Original_bw/*.*'   
files=glob.glob(path)   

new = ""
# traverse in the string  
for x in files: 
    new=new+x+"~"


new = list(new.split("~"))
l = len(new)-1
new.pop(l)

new2 = ""
# traverse in the string  
for y in files: 
    new2 += y+'~'

new2 = new2.replace('/home/adventum/Cairo_Data_Original_bw','')
new2 = list(new2.split("~"))
new2.pop()

z=0
for file in new:
    print(file)
    print("\n")
    a = cv2.imread(file)
    cv2.fastNlMeansDenoising(a,None,4,7,21)
    cv2.imwrite('/home/adventum/Desktop/new_denoised'+str(new2[z]),a)
    z = z+1
