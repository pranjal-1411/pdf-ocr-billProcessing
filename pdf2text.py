from PIL import Image 
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Sachin\AppData\Local\Tesseract-OCR\tesseract.exe'
import sys 
from pdf2image import convert_from_path 
import os 
  
PDF_file = "bill2.pdf"

pages = convert_from_path(PDF_file) 
 
image_counter = 1

for page in pages: 

    filename = "page_"+str(image_counter)+".jpg"

    page.save(filename, 'JPEG') 
    
    image_counter = image_counter + 1

    break
  
filelimit = image_counter-1

outfile = "out_text.txt"

f = open(outfile, "w") 

for i in range(1, filelimit + 1): 

    filename = "page_"+str(i)+".jpg"
           
    text = str(((pytesseract.image_to_string(Image.open(filename).convert("LA"))))) 

    text = text.replace('-\n', '')     
  
    f.write(text) 
 
f.close() 