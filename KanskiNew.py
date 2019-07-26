from io import StringIO 
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from nltk import sent_tokenize
import re


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

text = convert('/home/adventum/Downloads/kanskis.pdf')

text = text.lstrip()
text = text.rstrip()
text = text.lower()

#removing extra spaces in between words.
text= " ".join(text.split())

#converting text into list.
#sentences = sent_tokenize(text)

#extracting all headings from a pdf
def get_toc(pdf_path):
    infile = open(pdf_path, 'rb')
    parser = PDFParser(infile)
    document = PDFDocument(parser)

    toc = list()
    for (level,title,dest,a,structelem) in document.get_outlines():
        toc.append(level)
        toc.append(title)
    return toc

toc = get_toc('/home/adventum/Downloads/Kanski’s Clinical Ophthalmology.pdf')
indx =[]
for i in range(0,len(toc)):
    if i%2==0:
        indx.append(toc[i])
    if i%2==1:
        indx.append(toc[i].lower())
    
    

#searching for disease
def KanskiSearch(word):
    a = []
    b = indx.index(word)
    print('disease index:',b)
    a = toc[b:]
    
    c = a.index(4)+1
    c = a[c]
    print('next topic:',c)
    match = re.search(re.escape(word)+" (.+?) "+re.escape(c), text,flags=re.IGNORECASE)
 
    try:
        result = match.group(1)
    except:
        result = "no match found"
        
    f = open('/home/adventum/Downloads/a.txt', 'w')
    f.write(result)
 
KanskiSearch("diabetic retinopathy")
