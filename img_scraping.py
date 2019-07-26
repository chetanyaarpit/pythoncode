file1 = open("/home/adventum/Downloads/links.txt","rb")

links = file1.read()

file1.close()

links = str(links)

ll = links.split("/Content")
ll.pop(0)

for i in range(0,len(ll)):
    q = ll[i].rfind('---')
    le = len(ll[i])
    if '.jpg' in ll[i]:
        ll[i] = ll[i][:q]+'.jpg'+ ll[i][le:]
    elif '.png' in ll[i]:
        ll[i] = ll[i][:q]+'.png'+ ll[i][le:]
        

for i in range(0,len(ll)):
    ll[i] = "https://imagebank.asrs.org/Content"+ll[i]
    

jpg = ""
png = ""
gif = ""
#w3 = ".gif"

for j in range(0,len(ll)):
    if '.jpg' in ll[j]:
        jpg = jpg + ll[j] + " "
        
    elif '.png' in ll[j]: 
        png = png + ll[j] + " "
    
#    elif w3 in ll[j]:
 #       gif = gif + ll[j] + " "
    
jpg = jpg.split(" ")
jpg.pop()
png = png.split(" ")
png.pop()
#gif = gif.split(" ")

import urllib

jpg2 = ""
for i in range(0,len(jpg)):
    if 'https' in jpg[i]:
        jpg2 = jpg2 + jpg[i] + " "
        
jpg2 = jpg2.split(" ")
jpg2.pop()
        
jpg3 = ""        
for i in range(0,len(jpg2)):
    if '.jpg' in jpg2[i]:
        jpg3 = jpg3 + jpg2[i] + " "
        
jpg3 = jpg3.split(" ")
jpg3.pop()
jpg3.pop(57)
jpg3.pop(269)


png2 = ""
for i in range(0,len(png)):
    if 'https' in png[i]:
        png2 = png2 + png[i] + " "
        
png2 = png2.split(" ")
png2.pop()
        
png3 = ""        
for i in range(0,len(png2)):
    if '.png' in png2[i]:
        png3 = png3 + png2[i] + " "
        
png3 = png3.split(" ")
png3.pop()

#import urllib

for i in range(0,len(png3)):
    urllib.request.urlretrieve(png3[i],"/home/adventum/Downloads/img_scraping2/PngImg"+str(i)+".png")

for i in range(268,len(jpg3)):
    urllib.request.urlretrieve(jpg3[i],"/home/adventum/Downloads/img_scraping2/JpgImg"+str(i)+".jpg")
    
#for i in range(0,len(gif)):
 #   urllib.request.urlretrieve(gif[i],"/home/adventum/Downloads/img scraping/JpgImg"+str(i)+".gif")