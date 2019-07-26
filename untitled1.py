import os
from PIL import Image

def rotate_img(img_path, rt_degr):
     img = Image.open(img_path)
     return img.rotate(rt_degr)

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

listOfFiles = getListOfFiles('/home/adventum/Downloads/Master-OCT')

em = []
m = []
w = []
o = []
l = []

for i in range(0,len(listOfFiles)):
    if 'Extracted_Masks' in listOfFiles[i]:
        
        em.append(listOfFiles[i])
    
    if 'mask.png' in listOfFiles[i]:
        
        m.append(listOfFiles[i])
        
    if 'White' in listOfFiles[i]:
        
        w.append(listOfFiles[i])
        
    if 'original' in listOfFiles[i]:
        
        o.append(listOfFiles[i])
        
    if 'Labbled' in listOfFiles[i]:
        
        l.append(listOfFiles[i])
        
em2 = []
j = 0
for i in em:
    print(i)
    start = i.rfind('/')+1
    print(start)
    em2.append(i[start:])

fol = []
for root,dirs,files in os.walk('/home/adventum/Downloads/Master-OCT'):
    fol.append(root)

j=0
for i in em:
    im = rotate_img(em[i],5)
    os.mkdir()
    im.save('/home/adventum/Downloads/out/'+em2[j])
    j+=1

