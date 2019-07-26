import PyPDF2
import re
import io
from io import StringIO
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdocument import PDFDocument
from nltk import sent_tokenize
'''
pdf_file = open('/home/adventum/Downloads/Kanski’s Clinical Ophthalmology.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page1 = read_pdf.getPage(6)
page2 = read_pdf.getPage(7)
page3 = read_pdf.getPage(8)

page_content1 = page1.extractText()
page_content1 = page_content1.replace('.','')
page_content1 = page_content1.strip()
l1 = list(page_content1.split('\n'))

while("" in l1) :
    l1.remove("") 
    
while("  " in l1) :
    l1.remove("  ")

ls1=[]
for i in range(0,len(l1)):
    ls1.append(l1[i].lower())
ls1.pop()

del l1

page_content2 = page2.extractText()
page_content2 = page_content2.replace('.','')
page_content2 = page_content2.strip()
l2 = list(page_content2.split('\n'))

while("" in l2):
    l2.remove("") 

while("  " in l2): 
    l2.remove("  ")

ls2=[]
for i in range(0,len(l2)):
    ls2.append(l2[i].lower())
ls2.pop()

del l2

page_content3 = page3.extractText()
page_content3 = page_content3.replace('.','')
page_content3 = page_content3.strip()
l3 = list(page_content3.split('\n'))

while("" in l3): 
    l3.remove("") 
    
while("  " in l3): 
    l3.remove("  ")

ls3=[]
for i in range(0,len(l3)):
    ls3.append(l3[i].lower())
ls3.pop()

del l3
'''
a = open('/home/adventum/Downloads/toc1.txt')
a = a.read()
a = a.replace('.','')
a = a.strip()
l1 = list(a.split('\n'))
ls1=[]
for i in range(0,len(l1)):
    ls1.append(l1[i].lower())


b = open('/home/adventum/Downloads/toc2.txt')
b = b.read()
b = b.replace('.','')
b = b.strip()
l2 = list(b.split('\n'))
ls2=[]
for i in range(0,len(l2)):
    ls2.append(l2[i].lower())


c = open('/home/adventum/Downloads/toc3.txt')
c = c.read()
c = c.replace('.','')
c = c.strip()
l3 = list(c.split('\n'))
ls3=[]
for i in range(0,len(l3)):
    ls3.append(l3[i].lower())


toc = ls1+ls2+ls3

def KanskiSearch(word):
    for i in range(0,len(toc)):
        if word in toc[i]:
            print('topic found')
            #pg_no = toc[i][-2]+toc[i][-1]
            pg_no = ([int(s) for s in toc[i].split() if s.isdigit()])
            PageNo = pg_no[0]+11
            print('index:',i)
            pg_no2 = ([int(s) for s in toc[i+1].split() if s.isdigit()])
            pgend = pg_no2[0]+11
            next_topic = ''.join([i for i in toc[i+1] if not i.isdigit()])
            next_topic = next_topic.lstrip()
            next_topic = next_topic.rstrip()
            next_topic = next_topic.lower()
            break
    print('page_number_start:',PageNo)
    print('page_number_End:',pgend)
    print('next_topic:',next_topic)
    pages = []
    for i in range(PageNo,pgend+1):
        pages.append(i)
    print('allPages',pages)
    fp = open('/home/adventum/Downloads/Kanski’s Clinical Ophthalmology.pdf', 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    print(type(retstr))
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    page_no = pages
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        #print(pageNumber)
        if pageNumber in page_no:
            interpreter.process_page(page)
            data = retstr.getvalue()
            data = data.lstrip()
            data = data.rstrip()
            data = data.lower()
            data = data.replace('\u2002',' ')
            #removing extra spaces in between words.
            #data= " ".join(data.split())
            
    if word+'\n\nintroduction' in data:
        print('in if')
        
        strt = data.find(word+'\n\nintroduction')
        if next_topic+'\n\nintroduction' in data:
            end = data.find(next_topic+'\n\nintroduction')
        else:
            end = data.find(next_topic)
        print('str_strt:',strt)
        print('str_end:',end)
        data = data[strt:end]
        data= " ".join(data.split())
    else:
        print('in else')
        strt = data.find(word)
        if next_topic+'\n\nintroduction' in data:
            
            end = data.find(next_topic+'\n\nintroduction')
        else:
            end = data.find(next_topic)
        print('str_strt:',strt)
        print('str_end:',end)
        data = data[strt:end]
        data= " ".join(data.split())
    with open('/home/adventum/Downloads/disease.txt', 'w') as file:
        file.write(data)
    
    new=''
    if 'treatment' in data:
        tr = [m.start() for m in re.finditer('treatment', data)]
        print('tr:',tr)
        for i in range(0,len(tr)):
            t = tr[i]
            print('t'+str(i)+':',t)
            for j in range(8,100):
                if data[t+j]=='•':
                    print('inside if')
                    new = tr[i]
                    break
                elif data[t+j]=='○':
                    print('inside elif')
                    new = tr[i]
                    break
                
            if new!='':
                break
            else:
                print('treatment not found')
    if new!='':
        treatment = data[new:]
        if '•' in treatment:
            bullet = [m.start() for m in re.finditer('•', treatment)]
            print('allBullet',bullet)
            for i in range(0,len(bullet)):
                b = bullet[i]
                for j in range(50,300):
                    if treatment[b+j]=='•':
                        
                        continue
                    elif treatment[b+j]!='':
                        end = bullet[i]
                        break
                if end!='':
                    break
                else:
                    print('end not found')
            print(end)
        treat = treatment[:end]
        #treatment = " ".join(treatment.split())
        with open('/home/adventum/Downloads/treatment.txt','wb') as file:
            file.write(treat.encode('utf-8'))
    
KanskiSearch('diabetic retinopathy')
