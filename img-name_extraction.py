import glob
#import xlwt
from xlwt import Workbook 

wb = Workbook()

path = '/home/adventum/Downloads/images/*.png'   
files=glob.glob(path)   

new = ""
# traverse in the string  
for x in files: 
    new += x

new = new.replace('/home/adventum/Downloads/images/','')
new = list(new.split(".png"))
l = len(new)-1
new.pop(l)

sheet1 = wb.add_sheet('Sheet1')

for i in range(0,l):
    sheet1.write(i+1,0,new[i])
    wb.save('/home/adventum/Downloads/example.xls')
