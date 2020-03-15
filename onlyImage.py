from PIL import Image 
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Sachin\AppData\Local\Tesseract-OCR\tesseract.exe'
import sys 
from pdf2image import convert_from_path 
import os 
 
outfile = "out_text.txt"
  

f = open(outfile, "w") 
  
filename = "bill1.jpeg"
text = str(((pytesseract.image_to_string(Image.open(filename).convert('LA'))))) 
#print(pytesseract.image_to_boxes(Image.open(filename)))
text = text.replace('-\n', '')      
f.write(text) 

f.close() 