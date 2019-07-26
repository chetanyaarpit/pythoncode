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

while("" in l2) : 
    l2.remove("") 

while("  " in l2) : 
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

while("" in l3) : 
    l3.remove("") 
    
while("  " in l3) : 
    l3.remove("  ") 

ls3=[]
for i in range(0,len(l3)):
    ls3.append(l3[i].lower())
ls3.pop()

del l3

toc = ls1+ls2+ls3

def KanskiSearch(word):
    for i in range(0,len(toc)):
        if word in toc[i]:
            #pg_no = toc[i][-2]+toc[i][-1]
            pg_no = ([int(s) for s in toc[i].split() if s.isdigit()])
            PageNo = pg_no[0]+11
            print('index:',i)
            break
    print('page_number:',PageNo)
    fp = open('/home/adventum/Downloads/Kanski’s Clinical Ophthalmology.pdf', 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    print(type(retstr))
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    page_no = PageNo
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no:
            interpreter.process_page(page)

            data = retstr.getvalue()
            data = data.lstrip()
            data = data.rstrip()
            data = data.lower()

            #removing extra spaces in between words.
            data= " ".join(data.split())
            strt = data.find(word+' introduction')
            data = data[strt:]
                
            with open('/home/adventum/Downloads/a.txt', 'wb') as file:
                file.write(data.encode('utf-8'))
                data = ''
                retstr.truncate(0)
                retstr.seek(0)
   
KanskiSearch('anterior uveitis')
