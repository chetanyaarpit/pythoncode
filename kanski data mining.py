#import numpy as np
#import pandas as pd
#import pytesseract as tes
#import nltk
import re
import io
#import slate
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from nltk import sent_tokenize
#import docx 
#from nltk.tokenize import sent_tokenize
#import nltk
#nltk.download()
#import nltk
#nltk.download('punkt')
#from nltk.corpus import stopwords
#counting number of pages
#file = open('/home/chetanya/Downloads/kanskis.pdf','rb')
#parser = PDFParser(file)
#document = PDFDocument(parser)
#pgcount = resolve1(document.catalog['Pages'])['Count']
#pgcount
def extract_text_by_page(pdf_path):

    with open(pdf_path, 'rb') as fh:

        for page in PDFPage.get_pages(fh,caching=True,check_extractable=True):

            resource_manager = PDFResourceManager()

            fake_file_handle = io.StringIO()

            converter = TextConverter(resource_manager, fake_file_handle)

            page_interpreter = PDFPageInterpreter(resource_manager, converter)

            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()

            yield text

            # close open handles

            converter.close()

            fake_file_handle.close()

text = ""

#compliling all the pages.
for pages in extract_text_by_page('/home/adventum/Downloads/kanskis.pdf'):
    text = text + str(pages) 
    print('\n')
    print('\n')

#text cleaning
text = re.sub("[\(\[].*?[\)\]]", "", text)
#text = ''.join([i for i in text if not i.isdigit()])
text = text.replace('Fig.','')
#text = text.replace('•','')
#text = text.replace('○','')
text = text.lstrip()
text = text.rstrip()
text = text.lower()

#removing extra spaces in between words.
text= " ".join(text.split())

#converting text into list.
sentences = sent_tokenize(text)


def KanskiSearch(word):
    
        disease = [ line for line in sentences if word in line]
        
        if not disease:
            
            print("Term Not Found!")
            
        else:
            
            #Finding the disease
            print("Processing....")
            
            with open('/home/adventum/Downloads/a.txt', 'w') as f:
                
                for item in disease:
                    
                    f.write("%s\n" % item)
                    
                print("File written with all the information related to the term!")
            
            aa = open('/home/adventum/Downloads/a.txt', 'r')
            
            
            #Disease Treatment
            treatment = [ line for line in aa if 'treatment' in line]
            treatment2 = [ line for line in treatment if '•' in line]
            
            if not treatment2:
                
                    print("Treatment Not Found!")
                    
            else:
                
                    print("Processing....")
                    
                    with open('/home/adventum/Downloads/b.txt', 'w') as f:
                        
                        for item in treatment2:
                            
                            f.write("%s\n" % item)
                            
                        print("Treatment Printed!")
            
KanskiSearch("diabetic retinopathy")

# =============================================================================
# aa = open('/home/adventum/Downloads/a.txt', 'r')
# 
# def Treatment(word='treatment'):
#     x = [ line for line in aa if word in line]
#     if not x:
#             print("Treatment Not Found!")
#     else:
#         print("Processing....")
#         with open('/home/adventum/Downloads/b.txt', 'w') as f:
#             for item in x:
#                 f.write("%s\n" % item)
#         print("File written with all the information related to the term!")
# 
# Treatment()
# =============================================================================

#z = None
#z = [ line for line in sentences if 'adrsgh' in line]