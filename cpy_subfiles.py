import os
import shutil
#import re

count = 0

for root, dirs, files in os.walk('/home/adventum/Downloads/Master-OCT'):

    for file in files:
        path_file = os.path.join(root, file)
        #print(path_file)
        count += 1
        q = path_file.rfind('/')+1
        l = path_file.rfind('.')
        dsy = path_file[:q]+ 'file'+str(count)+ path_file[l:]
            
        print(dsy)
        os.rename(path_file, dsy)
        shutil.copy2(dsy, '/home/adventum/Downloads/cpy_MO')
            
#print('This is the total count: ')

#print(count)
