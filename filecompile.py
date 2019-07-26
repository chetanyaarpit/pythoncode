import os
import shutil

def fcount(path, map = {}):
  count = 0
  for f in os.listdir(path):
    child = os.path.join(path, f)
    
    
    if os.path.isdir(child):
      child_count = fcount(child, map)
      count += child_count +1 # unless include self
     # path_file = os.path.join()
      #shutil.copy2(path_file,'/home/adventum/Desktop/all')
      print(path)
      
      for root, dirs, files in os.walk(path):
          for file in files:
              path_file = os.path.join(root,file)
              shutil.copy2(path_file,'/home/adventum/Desktop/all')
                      
  map[path] = count
  return count

path = "/home/adventum/Downloads/new"
map = {}
print(fcount(path, map))
