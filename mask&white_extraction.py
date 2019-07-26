import os
import cv2
import shutil


l = []
l2 = []
l3 = []

for root, dirs, files in os.walk('/home/adventum/Downloads/Master-OCT'):    
    if 'Masks' in dirs:
        files = os.path.join(root,'Masks/mask.png')
        l.append(files)
        

c =1
for i in range(0,len(l)):
    shutil.copy2(l[i], '/home/adventum/Documents/mask&white/Masks/Img'+str(c)+'.png')
    c+=1
    

for root, dirs, files in os.walk('/home/adventum/Downloads/Master-OCT'):    
    if 'White_Mask' in dirs:
        files = os.path.join(root,'White_Mask/white_mask.png')
        l2.append(files)
        
c =1
for i in range(0,len(l2)):
    shutil.copy2(l2[i], '/home/adventum/Documents/mask&white/White/Img'+str(c)+'.png')
    c+=1
    

for root, dirs, files in os.walk('/home/adventum/Downloads/Master-OCT'):    
    if 'Labbled_img' in dirs:
        files = os.path.join(root,'Labbled_img/lable.png')
        l3.append(files)
        
c =1
for i in range(0,len(l3)):
    shutil.copy2(l3[i], '/home/adventum/Documents/mask&white/Labbled_Img/Img'+str(c)+'.png')
    c+=1