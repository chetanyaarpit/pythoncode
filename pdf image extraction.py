import os
import subprocess
import glob

def image_exporter(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cmd = ['pdfimages', '-png', pdf_path,
           '{}/prefix'.format(output_dir)]
    subprocess.call(cmd)
    print('Images extracted:')
    print(os.listdir(output_dir))
if __name__ == '__main__':
    path = '/home/adventum/OCT_NEW_Master/PDF+Doc/*.pdf'   
    files=glob.glob(path)   
    new = ""
    # traverse in the string  
    for x in files: 
        new += x
    
    new = new.split('/home')
    new.pop(0)
    for i in range(0,len(new)):
        new[i] = "/home"+new[i]
    for i in range(0,len(new)):    
        pdf_path = new[i]
        image_exporter(pdf_path, output_dir='/home/adventum/Downloads/imagesNew/'+'file'+str(i))
        
