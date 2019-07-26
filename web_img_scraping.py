from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://imagebank.asrs.org/discover/slideshow/2/25?q=oct#index=0')
bs = BeautifulSoup(html,'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
images = images + bs.find_all('img', {'src':re.compile('.png')})
images = images + bs.find_all('img', {'src':re.compile('.gif')})

l = ""

for image in images:
    l=l+image['src']+" "
    
    
ll = l.split(" ")
ll.pop()


for i in range(0,len(ll)):
    q = ll[i].rfind('---')
    le = len(ll[i])
    ll[i] = ll[i][:q]+'.jpg'+ ll[i][le:]


for i in range(0,len(ll)):
    ll[i] = "https://imagebank.asrs.org/Contents"+ll[i]
    

jpg = ""
png = ""
gif = ""
w1 = ".jpg"
w2 = ".png"
w3 = ".gif"

for j in range(0,len(ll)):
    if w1 in ll[j]:
        jpg = jpg + ll[j] + " "
        
    elif w2 in ll[j]: 
        png = png + ll[j] + " "
    
    elif w3 in ll[j]:
        gif = gif + ll[j] + " "
    
jpg = jpg.split(" ")
jpg.pop()
png = png.split(" ")
png.pop()
gif = gif.split(" ")

import urllib

for i in range(0,len(png)):
    urllib.request.urlretrieve(png[i],"/home/adventum/Downloads/img scraping/PngImg"+str(i)+".png")

for i in range(0,len(jpg)):
    urllib.request.urlretrieve(jpg[i],"/home/adventum/Downloads/img scraping/JpgImg"+str(i)+".jpg")
    
for i in range(0,len(gif)):
    urllib.request.urlretrieve(gif[i],"/home/adventum/Downloads/img scraping/JpgImg"+str(i)+".gif")
