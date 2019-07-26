
import os
import shutil

for root, dirs, files in os.walk('/home/adventum/Downloads'):
   for file in files:
      path_file = os.path.join(root,file)
      shutil.copy2(path_file,'/home/adventum/Desktop/all')

